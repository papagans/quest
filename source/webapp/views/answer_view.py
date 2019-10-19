from webapp.models import Poll, Choice
from django.views.generic import View, ListView, CreateView, DeleteView, UpdateView, DetailView
from webapp.forms import PollForm, ChoiceForm, QuestAnswerForm
from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, redirect


class AnswerView(ListView):
    context_object_name = 'answer'
    model = Choice
    template_name = 'answers/answers.html'
    paginate_by = 5
    paginate_orphans = 1


class AnswerForQuestionCreateView(CreateView):
    template_name = 'answers/create.html'
    form_class = QuestAnswerForm

    def form_valid(self, form):
        question_pk = self.kwargs.get('pk')
        question = get_object_or_404(Poll, pk=question_pk)
        question.answer.create(**form.cleaned_data)
        return redirect('question_view', pk=question_pk)


class AnswerCreateView(CreateView):
    model = Choice
    template_name = 'answers/create.html'
    form_class = ChoiceForm

    def get_success_url(self):
        return reverse('question_view', kwargs={'pk': self.object.answer.pk})


class AnswerDeleteView(DeleteView):
    model = Choice
    confirm_deletion = False

    # def get_redirect_url(self):
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('question_view', kwargs={'pk': self.object.answer.pk})

class AnswerUpdateView(UpdateView):
    model = Choice
    template_name = 'answers/update.html'
    form_class = ChoiceForm
    context_object_name = 'answer'

    def get_success_url(self):
        return reverse('answer_view', kwargs={'pk': self.object.answer.pk})