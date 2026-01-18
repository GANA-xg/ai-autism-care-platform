from django.db import models
from apps.children.models import Child
from django.conf import settings


class TherapyPlan(models.Model):
    child = models.ForeignKey(
        Child,
        on_delete=models.CASCADE,
        related_name='therapy_plans'
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    focus_area = models.CharField(
        max_length=100,
        help_text="e.g. Speech, Motor Skills, Social Interaction"
    )

    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.child.full_name} - {self.focus_area}"


class TherapyGoal(models.Model):
    plan = models.ForeignKey(
        TherapyPlan,
        on_delete=models.CASCADE,
        related_name='goals'
    )

    description = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description