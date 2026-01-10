from django.contrib import admin
from .models import TherapyPlan, TherapyGoal


class TherapyGoalInline(admin.TabularInline):
    model = TherapyGoal
    extra = 0


@admin.register(TherapyPlan)
class TherapyPlanAdmin(admin.ModelAdmin):
    list_display = ('child', 'focus_area', 'start_date', 'end_date')
    inlines = [TherapyGoalInline]