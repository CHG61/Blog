# admin.py
from django.contrib import admin
from .models import WorkExperience

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'content')
