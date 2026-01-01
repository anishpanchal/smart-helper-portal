from django.contrib import admin
from .models import AIQuery


@admin.register(AIQuery)
class AIQueryAdmin(admin.ModelAdmin):
    list_display = ['user', 'query', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'query', 'response']
    readonly_fields = ['created_at']
