from webapp.models import Poll, Choice
from django.views.generic import View, ListView, CreateView, DeleteView, UpdateView, DetailView
from webapp.forms import PollForm, ChoiceForm
from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy

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

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(object_list=object_list, **kwargs)
    #     # context['form'] = ArticleCommentForm()
    #     answers = context['question'].question()
    #     tags = self.tags()
    #     context['tags'] = tags
    #     self.paginate_comments_to_context(answers, context)
    #     return context
    #
    # def tags(self):
    #     tags = Choice.objects.all()
    #     print(tags)
    #     return tags

    def paginate_comments_to_context(self, comments, context):
        paginator = Paginator(comments, 3, 0)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['comments'] = page.object_list
        context['is_paginated'] = page.has_other_pages()

