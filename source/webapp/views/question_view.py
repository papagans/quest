from webapp.models import Poll, Answer, Choice
from django.views.generic import View, ListView, CreateView, DeleteView, UpdateView, DetailView
from webapp.forms import PollForm, ChoiceForm, QuestAnswerForm, AnswerForm
from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, View
from django.shortcuts import get_object_or_404, render, redirect

class IndexView(ListView):
    context_object_name = 'question'
    model = Poll
    template_name = 'questions/index.html'
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1


class QuestionCreateView(CreateView):
    model = Poll
    template_name = 'questions/create.html'
    form_class = PollForm

    def get_success_url(self):
        return reverse('index')


class QuestionDeleteView(DeleteView):
    model = Poll
    template_name = 'questions/delete.html'
    context_key = 'question'
    redirect_url = reverse_lazy('index')
    context_object_name = 'question'
    success_url = reverse_lazy('index')


class QuestionUpdateView(UpdateView):
    model = Poll
    template_name = 'questions/update.html'
    context_object_name = 'question'
    form_class = PollForm

    def get_success_url(self):
        return reverse('question_view', kwargs={'pk': self.object.pk})


class QuestionView(DetailView):
    template_name = 'questions/question.html'
    model = Poll
    context_object_name = 'question'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = QuestAnswerForm()
        answer = context['question'].answer.order_by()
        context['answer'] = answer
        # self.paginate_comments_to_context(answer, context)
        return context

class QuestionAnswerView(DetailView):
    template_name = 'quest_answer/quest_answer.html'
    model = Answer
    context_object_name = 'answer'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = QuestAnswerForm()
        answer = context['question'].answer.order_by()
        context['answer'] = answer
            # self.paginate_comments_to_context(answer, context)
        return context


class AnswersView(View):
    # def get(self, request, *args, **kwargs):
    #     poll = Poll.objects.get(id=kwargs['pk'])
    #     context = {'poll': poll}
    #     return render(request, 'quest_answer/quest_answer.html', context)

    def get(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, pk=kwargs['pk'])
        answer = poll.answer.all()
        context = {
            'poll': poll,
            'answer': answer
        }
        return render(request, 'quest_answer/quest_answer.html', context)

    def post(self, request, *args, **kwargs):
        pk = request.POST['answer']
        answer = get_object_or_404(Choice, pk=pk)
        print(answer)
        poll = get_object_or_404(Poll, pk=kwargs['pk'])
        Answer.objects.create(choices=answer, poll=poll)
        return redirect('index')