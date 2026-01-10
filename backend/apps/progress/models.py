from django.db import models
from apps.children.models import Child
from apps.therapy.models import TherapyPlan


class ProgressLog(models.Model):
    child = models.ForeignKey(
        Child,
        on_delete=models.CASCADE,
        related_name='progress_logs'
    )

    therapy_plan = models.ForeignKey(
        TherapyPlan,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    session_date = models.DateField()
    duration_minutes = models.PositiveIntegerField()

    engagement_level = models.IntegerField(
        help_text="Scale 1 (low) to 5 (high)"
    )

    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.child.full_name} - {self.session_date}"