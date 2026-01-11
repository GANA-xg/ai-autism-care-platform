from django.db import models
from apps.children.models import Child


class ScreeningSession(models.Model):
    RISK_CHOICES = (
        ('low', 'Low Risk'),
        ('medium', 'Medium Risk'),
        ('high', 'High Risk'),
    )

    child = models.ForeignKey(
        Child,
        on_delete=models.CASCADE,
        related_name='screenings'
    )

    age_in_months = models.PositiveIntegerField()
    total_score = models.IntegerField(default=0)
    risk_level = models.CharField(
        max_length=10,
        choices=RISK_CHOICES
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.child.full_name} - {self.risk_level}"


class ScreeningResponse(models.Model):
    session = models.ForeignKey(
        ScreeningSession,
        on_delete=models.CASCADE,
        related_name='responses'
    )

    question = models.CharField(max_length=255)
    answer = models.BooleanField()  # Yes / No