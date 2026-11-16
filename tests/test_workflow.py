"""Contratos observables de RF/RB; fixtures exclusivamente sintéticas."""

import copy
from decimal import Decimal
from cryptography.exceptions import InvalidTag
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.test import Client, TestCase
from django.urls import reverse
from orienta.catalogue import import_catalogue
from orienta.domain import compare, decrypt_response, encrypt_response, summarize
from orienta.models import (
    AuditEvent,
    Comparison,
    Datum,
    InterestResponse,
    Offer,
    Priority,
    Process,
    SavedOffer,
)


def sample_catalogue():
    return {
        "schema": 1,
        "source": {
            "url": "https://admision.udec.cl/fixture-e3/",
            "title": "Fixture sintética de contrato",
            "retrieved": "2026-11-16",
            "sha256": "a" * 64,
        },
        "offers": [
            {
                "code": "13001",
                "name": "Oferta sintética A",
                "campus": "Concepción",
                "cycle": 2027,
                "source_page": 1,
            },
            {
                "code": "13002",
                "name": "Oferta sintética B",
                "campus": "Chillán",
                "cycle": 2027,
                "source_page": 1,
            },
        ],
    }


class WorkflowTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        import_catalogue(sample_catalogue())
        cls.user = User.objects.create_user("alfa_sintetico", password="Clave-de-prueba-95!")
        cls.process = Process.objects.create(owner=cls.user)
        cls.other = User.objects.create_user("beta_sintetico", password="Clave-de-prueba-96!")
        cls.other_process = Process.objects.create(owner=cls.other)

    def setUp(self):
        self.client.force_login(self.user)
        self.a, self.b = list(Offer.objects.order_by("code"))

    def test_RF01_create_return_without_civil_identifier(self):
        self.client.logout()
        result = self.client.post(
            reverse("account"),
            {"alias": "nuevo_sintetico", "password": "Otra-clave-prueba-97!", "mode": "create"},
            follow=True,
        )
        self.assertEqual(result.status_code, 200)
        self.assertTrue(Process.objects.filter(owner__username="nuevo_sintetico").exists())
        self.client.post(reverse("logout"))
        self.assertEqual(
            self.client.post(
                reverse("account"),
                {"alias": "nuevo_sintetico", "password": "Otra-clave-prueba-97!", "mode": "login"},
            ).status_code,
            302,
        )

    def test_RF01_invalid_duplicate_and_wrong_credentials(self):
        self.client.logout()
        for data in [
            {"alias": "xx", "password": "short", "mode": "create"},
            {"alias": self.user.username, "password": "Clave-de-prueba-95!", "mode": "create"},
            {"alias": self.user.username, "password": "Incorrecta-clave-99!", "mode": "login"},
        ]:
            with self.subTest(data={k: v for k, v in data.items() if k != "password"}):
                result = self.client.post(reverse("account"), data)
                self.assertEqual(result.status_code, 200)
                self.assertNotIn("_auth_user_id", self.client.session)
        self.assertEqual(User.objects.count(), 2)

    def test_account_protocol_and_session_attempt_limit(self):
        self.client.logout()
        self.assertEqual(self.client.put(reverse("account")).status_code, 405)
        self.assertEqual(
            self.client.post(
                reverse("account"),
                {"alias": "alias_correcto", "password": "Clave-de-prueba-95!", "mode": "unknown"},
            ).status_code,
            400,
        )
        session = self.client.session
        session["login_attempts"] = 10
        session.save()
        self.assertEqual(self.client.post(reverse("account"), {}).status_code, 429)

    def test_RF02_RF03_complete_versioned_interests_survive_logout(self):
        answers = {f"q{i}": 4 if i % 2 else 2 for i in range(1, 13)}
        self.assertEqual(self.client.post(reverse("interests"), answers).status_code, 302)
        self.assertEqual(self.process.responses.count(), 12)
        response = self.process.responses.get(item=1)
        self.assertEqual(decrypt_response(response), 4)
        self.assertNotEqual(bytes(response.encrypted_value), b"4")
        self.client.post(reverse("logout"))
        self.client.post(
            reverse("account"),
            {"alias": self.user.username, "password": "Clave-de-prueba-95!", "mode": "login"},
        )
        page = self.client.get(reverse("interests"))
        self.assertContains(page, "Lo que expresaste")
        self.assertEqual([x["mean"] for x in page.context["summary"]], [3.0] * 6)

    def test_RF02_invalid_incomplete_submission_does_not_persist(self):
        for data in [{"q1": 9}, {f"q{i}": 0 for i in range(1, 13)}]:
            self.assertEqual(self.client.post(reverse("interests"), data).status_code, 400)
        self.assertEqual(self.process.responses.count(), 0)

    def test_CI2_random_nonces_tamper_and_binding(self):
        first = encrypt_response(self.process.pk, 1, 4)
        second = encrypt_response(self.process.pk, 1, 4)
        self.assertNotEqual(first, second)
        row = InterestResponse.objects.create(process=self.process, item=1, encrypted_value=first)
        self.assertEqual(decrypt_response(row), 4)
        for item, process_id, blob in [
            (2, self.process.pk, first),
            (1, self.other_process.pk, first),
            (1, self.process.pk, first[:-1] + bytes([first[-1] ^ 1])),
        ]:
            row.item, row.process_id, row.encrypted_value = item, process_id, blob
            with self.subTest(item=item, process=str(process_id)):
                with self.assertRaises(InvalidTag):
                    decrypt_response(row)

    def test_CI2_corrupt_payload_fails_closed_in_interface(self):
        InterestResponse.objects.create(
            process=self.process, item=1, encrypted_value=b"corrupted" * 4
        )
        self.assertEqual(self.client.get(reverse("interests")).status_code, 503)

    def test_RF04_priorities_remain_undefined_until_declared(self):
        self.assertEqual(self.process.priorities.count(), 0)
        self.assertEqual(
            self.client.post(
                reverse("priorities"), {"duracion": 3, "arancel": "", "empleabilidad": 1}
            ).status_code,
            302,
        )
        self.assertEqual(
            dict(self.process.priorities.values_list("dimension", "level")),
            {"duracion": 3, "empleabilidad": 1},
        )
        self.assertEqual(self.client.post(reverse("priorities"), {"duracion": 9}).status_code, 400)
        self.client.post(reverse("priorities"), {})
        self.assertEqual(self.process.priorities.count(), 0)

    def test_RF05_RF06_catalogue_filters_and_provenance(self):
        result = self.client.get(reverse("catalog"), {"campus": "Chillán"})
        self.assertContains(result, "Oferta sintética B")
        self.assertNotContains(result, "Oferta sintética A")
        self.assertEqual(
            len(self.client.get(reverse("catalog"), {"q": "no-existe"}).context["offers"]), 0
        )
        detail = self.client.get(reverse("detail", args=[self.a.pk]))
        self.assertContains(detail, "Información no disponible")
        self.assertContains(detail, "https://admision.udec.cl/fixture-e3/")

    def test_RF07a_RF07b_idempotent_save_and_remove(self):
        for _ in range(2):
            self.assertEqual(
                self.client.post(reverse("save_offer", args=[self.a.pk])).status_code, 302
            )
        self.assertEqual(SavedOffer.objects.filter(process=self.process).count(), 1)
        self.assertContains(self.client.get(reverse("saved")), "Oferta sintética A")
        self.client.post(reverse("remove_offer", args=[self.a.pk]))
        self.assertEqual(self.process.saved.count(), 0)

    def test_RF08_duplicate_or_missing_pair_cannot_replace_valid_pair(self):
        for data in [{"offer_a": self.a.pk}, {"offer_a": self.a.pk, "offer_b": self.a.pk}]:
            self.assertEqual(self.client.post(reverse("comparison"), data).status_code, 400)
        self.assertFalse(Comparison.objects.exists())

    def test_RF09_RF10_missing_fields_and_priorities_without_winner(self):
        Priority.objects.create(process=self.process, dimension="duracion", level=3)
        self.client.post(reverse("comparison"), {"offer_a": self.a.pk, "offer_b": self.b.pk})
        page = self.client.get(reverse("comparison"))
        self.assertContains(page, "Prioridad alta")
        self.assertContains(page, "Información no disponible")
        self.assertContains(page, "No se reemplaza por cero")
        self.assertEqual(Comparison.objects.get(process=self.process).offer_b_id, self.b.pk)

    def test_RF09_compatible_values_and_nonhomologous_periods(self):
        a = Datum.objects.get(offer=self.a, dimension="duracion")
        b = Datum.objects.get(offer=self.b, dimension="duracion")
        for d, value in [(a, 10), (b, 12)]:
            d.value, d.period = Decimal(value), "Plan vigente"
            d.save()
        rows = compare(self.a, self.b, {})
        self.assertIn("2.00 semestres", rows[0]["reason"])
        b.period = "Plan histórico"
        b.save()
        self.assertIn("no son homologables", compare(self.a, self.b, {})[0]["reason"])
        with self.assertRaises(ValueError):
            compare(self.a, self.a, {})

    def test_RF11_no_cross_owner_read_or_delete(self):
        for route in ["snapshot", "delete"]:
            url = reverse(route, args=[self.other_process.pk])
            with self.subTest(url=url):
                self.assertEqual(self.client.get(url).status_code, 404)
                self.assertEqual(
                    self.client.post(url, {"confirm": "ELIMINAR"}).status_code,
                    404 if route == "delete" else 405,
                )
        self.assertTrue(User.objects.filter(pk=self.other.pk).exists())
        self.assertEqual(
            self.client.get(reverse("snapshot", args=[self.process.pk])).status_code, 200
        )

    def test_RF19_own_confirmed_deletion_cascades(self):
        SavedOffer.objects.create(process=self.process, offer=self.a)
        Priority.objects.create(process=self.process, dimension="arancel", level=2)
        InterestResponse.objects.create(
            process=self.process, item=1, encrypted_value=encrypt_response(self.process.pk, 1, 2)
        )
        url = reverse("delete", args=[self.process.pk])
        self.assertEqual(self.client.get(url).status_code, 200)
        self.assertEqual(self.client.post(url, {"confirm": "no"}).status_code, 400)
        self.assertEqual(self.client.post(url, {"confirm": "ELIMINAR"}).status_code, 302)
        self.assertFalse(User.objects.filter(pk=self.user.pk).exists())
        self.assertFalse(Process.objects.filter(pk=self.process.pk).exists())
        self.assertFalse(InterestResponse.objects.exists())
        self.assertFalse(SavedOffer.objects.exists())
        self.assertEqual(AuditEvent.objects.filter(kind="account_deleted").count(), 1)

    def test_RNFS01_authentication_expiry_and_csrf(self):
        client = Client(enforce_csrf_checks=True)
        self.assertEqual(client.post(reverse("account"), {}).status_code, 403)
        client.force_login(self.user)
        self.assertEqual(client.post(reverse("save_offer", args=[self.a.pk])).status_code, 403)
        session = self.client.session
        session.set_expiry(-1)
        session.save()
        self.assertEqual(self.client.get(reverse("dashboard")).status_code, 302)

    def test_RNFS04_headers_and_error_correlation(self):
        response = self.client.get("/ruta-inexistente/")
        self.assertEqual(response.status_code, 404)
        self.assertIn("frame-ancestors 'none'", response["Content-Security-Policy"])
        self.assertEqual(response["Cache-Control"], "no-store")
        self.assertEqual(len(response["X-Request-ID"]), 32)
        self.assertEqual(self.client.get(reverse("health")).json()["status"], "ok")

    def test_RF18_catalogue_atomic_rejection_and_repeatable_import(self):
        payload = sample_catalogue()
        payload["offers"].append(copy.deepcopy(payload["offers"][0]))
        with self.assertRaises(ValidationError):
            import_catalogue(payload)
        self.assertEqual(Offer.objects.count(), 2)
        self.assertEqual(import_catalogue(sample_catalogue()), 2)
        self.assertEqual(Offer.objects.count(), 2)
        payload = sample_catalogue()
        payload["offers"] = payload["offers"][:1]
        import_catalogue(payload)
        self.assertEqual(Offer.objects.filter(active=True).count(), 1)

    def test_RF18_rejects_invalid_source_schema_fields(self):
        variants = [{}, {**sample_catalogue(), "schema": 99}, {**sample_catalogue(), "offers": []}]
        for field, value in [
            ("url", "javascript:alert(1)"),
            ("sha256", "invalid"),
            ("retrieved", "tomorrow"),
            ("title", ""),
        ]:
            p = sample_catalogue()
            p["source"][field] = value
            variants.append(p)
        for field, value in [
            ("code", "wrong"),
            ("cycle", 2026),
            ("name", ""),
            ("campus", "No existe"),
            ("source_page", 0),
        ]:
            p = sample_catalogue()
            p["offers"][0][field] = value
            variants.append(p)
        for payload in variants:
            with self.subTest(payload=payload):
                with self.assertRaises(ValidationError):
                    import_catalogue(payload)

    def test_CI1_database_blocks_duplicates_and_self_comparison(self):
        SavedOffer.objects.create(process=self.process, offer=self.a)
        for model, values in [
            (SavedOffer, {"process": self.process, "offer": self.a}),
            (Comparison, {"process": self.process, "offer_a": self.a, "offer_b": self.a}),
            (Priority, {"process": self.process, "dimension": "duracion", "level": 4}),
        ]:
            with self.subTest(model=model.__name__):
                with self.assertRaises(IntegrityError), transaction.atomic():
                    model.objects.create(**values)

    def test_summary_validates_scale_and_complete_items(self):
        for values in [{}, {i: 9 for i in range(1, 13)}, {i: True for i in range(1, 13)}]:
            with self.assertRaises(ValueError):
                summarize(values)

    def test_mutations_reject_get_and_other_methods(self):
        for route, args in [
            ("save_offer", [self.a.pk]),
            ("remove_offer", [self.a.pk]),
            ("logout", []),
        ]:
            self.assertEqual(self.client.get(reverse(route, args=args)).status_code, 405)
        for route in ("interests", "priorities", "comparison"):
            self.assertEqual(self.client.put(reverse(route)).status_code, 405)
        self.assertEqual(
            self.client.put(reverse("delete", args=[self.process.pk])).status_code, 405
        )
