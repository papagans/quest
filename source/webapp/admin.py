from django.contrib import admin
from webapp.models import Poll, Choice


class PollAdmin(admin.ModelAdmin):
    list_display = ['question', 'created_at']
    list_filter = ['question']
    search_fields = ['question']
    fields = ['question', 'created_at']
    readonly_fields = ['created_at']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['answer']
    list_filter = ['answer']
    search_fields = ['answer']
    fields = ['answer']


admin.site.register(Poll)
admin.site.register(Choice)
