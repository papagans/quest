from django.contrib import admin
from webapp.models import Poll, Choice, Answer


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


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['poll', 'choices', 'created_at']
    list_filter = ['poll']
    search_fields = ['poll']
    fields = ['poll', 'choices', 'created_at']
    readonly_fields = ['created_at']


admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Answer)
