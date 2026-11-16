from django import forms
from django.contrib.auth.password_validation import validate_password
from .domain import DIMENSIONS, ITEMS
from .models import Offer


class AccountForm(forms.Form):
    alias = forms.RegexField(
        r"^[a-zA-Z0-9_-]{4,32}$",
        label="Alias",
        max_length=32,
        help_text="Usa un alias de prueba, sin nombre ni RUT.",
    )
    password = forms.CharField(
        label="Contraseña",
        min_length=12,
        max_length=128,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )

    def clean_password(self):
        value = self.cleaned_data["password"]
        if self.data.get("mode") == "create":
            validate_password(value)
        return value


class InterestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for number, _label, text in ITEMS:
            self.fields[f"q{number}"] = forms.TypedChoiceField(
                label=text,
                choices=[
                    ("", "Selecciona una respuesta"),
                    *[
                        (i, f"{i} · {label}")
                        for i, label in enumerate(
                            ["Nada", "Poco", "Algo", "Bastante", "Mucho"], start=1
                        )
                    ],
                ],
                coerce=int,
            )


class PriorityForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, label in [("ubicacion", "Ubicación"), *DIMENSIONS]:
            self.fields[key] = forms.TypedChoiceField(
                label=label,
                choices=[("", "Sin definir"), (1, "Baja"), (2, "Media"), (3, "Alta")],
                coerce=int,
                empty_value=None,
                required=False,
            )


class PairForm(forms.Form):
    offer_a = forms.ModelChoiceField(
        queryset=Offer.objects.filter(active=True).select_related("career", "campus"),
        label="Primera oferta",
    )
    offer_b = forms.ModelChoiceField(
        queryset=Offer.objects.filter(active=True).select_related("career", "campus"),
        label="Segunda oferta",
    )

    def clean(self):
        values = super().clean()
        if (
            values.get("offer_a")
            and values.get("offer_b")
            and values["offer_a"].pk == values["offer_b"].pk
        ):
            raise forms.ValidationError("Elige exactamente dos ofertas distintas.")
        return values
