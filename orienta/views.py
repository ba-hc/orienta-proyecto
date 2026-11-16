import logging
from cryptography.exceptions import InvalidTag
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError, transaction
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET, require_POST
from .domain import compare, decrypt_response, encrypt_response, summarize
from .forms import AccountForm, InterestForm, PairForm, PriorityForm
from .models import (
    AuditEvent,
    Campus,
    Comparison,
    InterestResponse,
    Offer,
    Priority,
    Process,
    SavedOffer,
)

logger = logging.getLogger("orienta")


def account(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method not in ("GET", "POST"):
        return HttpResponseNotAllowed(["GET", "POST"])
    form = AccountForm(request.POST if request.method == "POST" else None)
    attempts = request.session.get("login_attempts", 0)
    if request.method == "POST":
        if attempts >= 10:
            return render(
                request,
                "orienta/account.html",
                {
                    "form": form,
                    "notice": "Demasiados intentos en esta sesión. Cierra el navegador y vuelve a intentarlo en el entorno local.",
                },
                status=429,
            )
        if form.is_valid():
            alias, password = form.cleaned_data["alias"], form.cleaned_data["password"]
            mode = request.POST.get("mode")
            if mode == "create":
                try:
                    with transaction.atomic():
                        user = User.objects.create_user(username=alias, password=password)
                        Process.objects.create(owner=user)
                except IntegrityError:
                    form.add_error(
                        "alias", "Este alias ya está ocupado. Elige otro o retoma tu proceso."
                    )
                else:
                    login(request, user)
                    AuditEvent.objects.create(kind="account_created")
                    return redirect("dashboard")
            elif mode == "login":
                user = authenticate(request, username=alias, password=password)
                if user:
                    login(request, user)
                    request.session["login_attempts"] = 0
                    AuditEvent.objects.create(kind="session_started")
                    return redirect("dashboard")
                request.session["login_attempts"] = attempts + 1
                form.add_error(None, "Alias o contraseña incorrectos. Revisa ambos datos.")
            else:
                return HttpResponse("Operación inválida", status=400)
    return render(request, "orienta/account.html", {"form": form})


def own_process(request, process_id=None):
    filters = {"owner": request.user}
    if process_id is not None:
        filters["pk"] = process_id
    return get_object_or_404(Process, **filters)


@login_required
@require_GET
def dashboard(request):
    process = own_process(request)
    return render(
        request,
        "orienta/dashboard.html",
        {
            "process": process,
            "answered": process.responses.count(),
            "priority_count": process.priorities.count(),
            "saved_count": process.saved.count(),
            "comparison": Comparison.objects.filter(process=process).first(),
        },
    )


@login_required
def interests(request):
    process = own_process(request)
    if request.method not in ("GET", "POST"):
        return HttpResponseNotAllowed(["GET", "POST"])
    try:
        values = {r.item: decrypt_response(r) for r in process.responses.all()}
    except (InvalidTag, ValueError):
        logger.error("interest_integrity_failed")
        return render(
            request,
            "orienta/error.html",
            {
                "notice": "No se pudo verificar la integridad de tus respuestas. No se mostrará un resultado. Contacta al responsable de la demo."
            },
            status=503,
        )
    form = InterestForm(
        request.POST if request.method == "POST" else None,
        initial={f"q{k}": v for k, v in values.items()},
    )
    if request.method == "POST" and form.is_valid():
        with transaction.atomic():
            for i in range(1, 13):
                InterestResponse.objects.update_or_create(
                    process=process,
                    item=i,
                    defaults={
                        "encrypted_value": encrypt_response(
                            process.pk, i, form.cleaned_data[f"q{i}"]
                        )
                    },
                )
            process.save(update_fields=["updated_at"])
        AuditEvent.objects.create(kind="interests_saved")
        return redirect("interests")
    summary = summarize(values) if len(values) == 12 else []
    return render(
        request,
        "orienta/interests.html",
        {"form": form, "summary": summary, "process": process},
        status=400 if request.method == "POST" and form.errors else 200,
    )


@login_required
def priorities(request):
    process = own_process(request)
    if request.method not in ("GET", "POST"):
        return HttpResponseNotAllowed(["GET", "POST"])
    form = PriorityForm(
        request.POST if request.method == "POST" else None,
        initial=dict(process.priorities.values_list("dimension", "level")),
    )
    if request.method == "POST" and form.is_valid():
        with transaction.atomic():
            for key, level in form.cleaned_data.items():
                if level is None:
                    Priority.objects.filter(process=process, dimension=key).delete()
                else:
                    Priority.objects.update_or_create(
                        process=process, dimension=key, defaults={"level": level}
                    )
            process.save(update_fields=["updated_at"])
        return redirect("dashboard")
    return render(
        request,
        "orienta/priorities.html",
        {"form": form},
        status=400 if request.method == "POST" and form.errors else 200,
    )


@login_required
@require_GET
def catalog(request):
    offers = Offer.objects.filter(active=True).select_related("career", "campus", "source")
    query = request.GET.get("q", "")[:120].strip()
    campus = request.GET.get("campus", "")[:70]
    if query:
        offers = offers.filter(Q(career__name__icontains=query) | Q(code__icontains=query))
    if campus:
        offers = offers.filter(campus__name=campus)
    saved = set(own_process(request).saved.values_list("offer_id", flat=True))
    return render(
        request,
        "orienta/catalog.html",
        {
            "offers": offers,
            "campuses": Campus.objects.all(),
            "query": query,
            "selected_campus": campus,
            "saved": saved,
            "count": offers.count(),
        },
    )


@login_required
@require_GET
def detail(request, offer_id):
    offer = get_object_or_404(
        Offer.objects.select_related("career", "campus", "source").prefetch_related("data__source"),
        pk=offer_id,
        active=True,
    )
    return render(
        request,
        "orienta/detail.html",
        {"offer": offer, "saved": own_process(request).saved.filter(offer=offer).exists()},
    )


@login_required
@require_POST
def save_offer(request, offer_id):
    offer = get_object_or_404(Offer, pk=offer_id, active=True)
    process = own_process(request)
    SavedOffer.objects.get_or_create(process=process, offer=offer)
    return redirect("saved")


@login_required
@require_POST
def remove_offer(request, offer_id):
    SavedOffer.objects.filter(process=own_process(request), offer_id=offer_id).delete()
    return redirect("saved")


@login_required
@require_GET
def saved(request):
    entries = own_process(request).saved.select_related("offer__career", "offer__campus").all()
    return render(request, "orienta/saved.html", {"entries": entries})


@login_required
def comparison(request):
    process = own_process(request)
    if request.method not in ("GET", "POST"):
        return HttpResponseNotAllowed(["GET", "POST"])
    current = (
        Comparison.objects.filter(process=process)
        .select_related(
            "offer_a__career",
            "offer_a__campus",
            "offer_a__source",
            "offer_b__career",
            "offer_b__campus",
            "offer_b__source",
        )
        .first()
    )
    initial = {"offer_a": current.offer_a_id, "offer_b": current.offer_b_id} if current else {}
    form = PairForm(request.POST if request.method == "POST" else None, initial=initial)
    if request.method == "POST" and form.is_valid():
        Comparison.objects.update_or_create(process=process, defaults=form.cleaned_data)
        AuditEvent.objects.create(kind="comparison_saved")
        return redirect("comparison")
    rows = (
        compare(
            current.offer_a,
            current.offer_b,
            dict(process.priorities.values_list("dimension", "level")),
        )
        if current
        else []
    )
    return render(
        request,
        "orienta/comparison.html",
        {
            "form": form,
            "comparison": current,
            "rows": rows,
            "location_priority": process.priorities.filter(dimension="ubicacion")
            .values_list("level", flat=True)
            .first(),
        },
        status=400 if request.method == "POST" and form.errors else 200,
    )


@login_required
def delete_process(request, process_id):
    process = own_process(request, process_id)
    if request.method not in ("GET", "POST"):
        return HttpResponseNotAllowed(["GET", "POST"])
    if request.method == "POST":
        if request.POST.get("confirm") != "ELIMINAR":
            return render(
                request,
                "orienta/delete.html",
                {"process": process, "notice": "Escribe ELIMINAR para confirmar la supresión."},
                status=400,
            )
        user = request.user
        with transaction.atomic():
            user.delete()
            AuditEvent.objects.create(kind="account_deleted")
        logout(request)
        return redirect("account")
    return render(request, "orienta/delete.html", {"process": process})


@login_required
@require_GET
def process_snapshot(request, process_id):
    process = own_process(request, process_id)
    return JsonResponse(
        {
            "id": str(process.pk),
            "instrument_version": process.instrument_version,
            "responses_count": process.responses.count(),
            "priorities": dict(process.priorities.values_list("dimension", "level")),
            "saved": list(process.saved.values_list("offer__code", flat=True)),
        }
    )


@require_POST
def end_session(request):
    logout(request)
    return redirect("account")


@require_GET
def health(request):
    from django.db import connection

    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        cursor.fetchone()
    return JsonResponse({"status": "ok", "mode": "academic-local"})
