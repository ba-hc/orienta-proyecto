import uuid
from django.conf import settings
from django.db import models


class Campus(models.Model):
    name = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.name


class Career(models.Model):
    name = models.CharField(max_length=180, unique=True)


class Source(models.Model):
    url = models.URLField(max_length=700, unique=True)
    title = models.CharField(max_length=180)
    retrieved = models.DateField()
    sha256 = models.CharField(max_length=64)


class Offer(models.Model):
    code = models.CharField(max_length=20)
    career = models.ForeignKey(Career, on_delete=models.PROTECT)
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT)
    cycle = models.PositiveIntegerField()
    source = models.ForeignKey(Source, on_delete=models.PROTECT)
    source_page = models.PositiveIntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["code", "cycle"], name="offer_code_cycle_unique")
        ]
        ordering = ["career__name", "campus__name"]

    def __str__(self):
        return f"{self.career.name} · {self.campus.name} ({self.code})"


class Datum(models.Model):
    offer = models.ForeignKey(Offer, related_name="data", on_delete=models.CASCADE)
    dimension = models.CharField(max_length=30)
    value = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    unit = models.CharField(max_length=35)
    period = models.CharField(max_length=35)
    source = models.ForeignKey(Source, on_delete=models.PROTECT)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["offer", "dimension"], name="datum_offer_dimension_unique"
            )
        ]


class Process(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    instrument_version = models.CharField(max_length=45, default="ORIENTA-EXPLORA-1")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class InterestResponse(models.Model):
    process = models.ForeignKey(Process, related_name="responses", on_delete=models.CASCADE)
    item = models.PositiveSmallIntegerField()
    encrypted_value = models.BinaryField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["process", "item"], name="response_process_item_unique")
        ]


class Priority(models.Model):
    process = models.ForeignKey(Process, related_name="priorities", on_delete=models.CASCADE)
    dimension = models.CharField(max_length=30)
    level = models.PositiveSmallIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["process", "dimension"], name="priority_process_dimension_unique"
            ),
            models.CheckConstraint(condition=models.Q(level__lte=3), name="priority_level_range"),
        ]


class SavedOffer(models.Model):
    process = models.ForeignKey(Process, related_name="saved", on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["process", "offer"], name="saved_process_offer_unique")
        ]


class Comparison(models.Model):
    process = models.OneToOneField(Process, on_delete=models.CASCADE)
    offer_a = models.ForeignKey(Offer, related_name="comparisons_a", on_delete=models.CASCADE)
    offer_b = models.ForeignKey(Offer, related_name="comparisons_b", on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=~models.Q(offer_a=models.F("offer_b")), name="comparison_distinct_offers"
            )
        ]


class AuditEvent(models.Model):
    """Solo tipo/fecha/correlación; sin identidad ni respuestas."""

    kind = models.CharField(max_length=35)
    correlation = models.UUIDField(default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
