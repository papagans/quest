from webapp.models import Poll, Choice
from django.views.generic import View, ListView, CreateView, DeleteView, UpdateView, DetailView
from webapp.forms import PollForm, ChoiceForm
from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy


class AnswerView(ListView):
    context_object_name = 'answer'
    model = Choice
    template_name = 'answers/answers.html'
    paginate_by = 5
    paginate_orphans = 1


class AnswerCreateView(CreateView):
    model = Choice
    template_name = 'answers/answers.html'
    form_class = ChoiceForm

    def get_success_url(self):
        return reverse('answer_view', kwargs={'pk': self.object.answer.pk})


class AnswerDeleteView:
    pass


class AnswerUpdateView(UpdateView):
    model = Choice
    template_name = 'answers/answers.html'
    form_class = ChoiceForm
    context_object_name = 'answer'

    def get_success_url(self):
        return reverse('answer_view', kwargs={'pk': self.object.answer.pk})