from django.contrib import admin
from .models import ProgressLog


@admin.register(ProgressLog)
class ProgressLogAdmin(admin.ModelAdmin):
    list_display = ('child', 'session_date', 'duration_minutes', 'engagement_level')
    list_filter = ('session_date',)