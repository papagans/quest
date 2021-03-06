"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import IndexView,  QuestionCreateView, QuestionDeleteView, QuestionUpdateView, QuestionView, \
     AnswerCreateView, AnswerDeleteView, AnswerUpdateView, AnswerForQuestionCreateView, AnswersView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('question/<int:pk>/', QuestionView.as_view(), name='question_view'),
    path('question/add/', QuestionCreateView.as_view(), name='add_question'),
    path('question/<int:pk>/edit/', QuestionUpdateView.as_view(), name='question_update'),
    path('question/<int:pk>/delete/', QuestionDeleteView.as_view(), name='question_delete'),
    path('answer/add/', AnswerCreateView.as_view(), name='answer_add'),
    path('answer/<int:pk>/edit/', AnswerUpdateView.as_view(), name='answer_update'),
    path('answer/<int:pk>/delete/', AnswerDeleteView.as_view(), name='answer_delete'),
    path('answer/<int:pk>/add-answer/', AnswerForQuestionCreateView.as_view(), name='question_answer_create'),
    path('answer/<int:pk>/add-quest_answer/', AnswersView.as_view(), name='quest_answer')
]
