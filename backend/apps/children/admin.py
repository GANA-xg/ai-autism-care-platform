from django.contrib import admin
from .models import Child


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'parent', 'gender', 'diagnosis_status')
    list_filter = ('gender', 'diagnosis_status')
    search_fields = ('full_name',)