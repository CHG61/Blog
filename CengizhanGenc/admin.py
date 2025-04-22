from django.contrib import admin
from .models import HomepageHighlight

@admin.register(HomepageHighlight)
class HomepageHighlightAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'content')
