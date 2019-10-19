from django import forms
from webapp.models import Poll, Choice

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = ['created_at']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        exclude = ['created_at']


class QuestAnswerForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['answer']