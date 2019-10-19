from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=200, null=False, blank=False, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey('webapp.Poll', related_name='ответ', on_delete=models.CASCADE,
                                verbose_name='Вопрос')
    answer = models.TextField(max_length=400, null=False, blank=False, verbose_name='Ответ')

    def __str__(self):
        return self.answer