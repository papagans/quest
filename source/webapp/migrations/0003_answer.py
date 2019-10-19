# Generated by Django 2.2 on 2019-10-19 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20191019_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('choices', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice', to='webapp.Choice', verbose_name='Ответ')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_question', to='webapp.Poll', verbose_name='Вопрос')),
            ],
        ),
    ]
