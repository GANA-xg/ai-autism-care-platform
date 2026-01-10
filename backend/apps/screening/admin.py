from django.contrib import admin
from .models import ScreeningSession, ScreeningResponse


class ScreeningResponseInline(admin.TabularInline):
    model = ScreeningResponse
    extra = 0


@admin.register(ScreeningSession)
class ScreeningSessionAdmin(admin.ModelAdmin):
    list_display = ('child', 'risk_level', 'total_score', 'created_at')
    list_filter = ('risk_level',)
    inlines = [ScreeningResponseInline]