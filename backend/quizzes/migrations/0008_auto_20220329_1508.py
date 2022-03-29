# Generated by Django 3.1 on 2022-03-29 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0007_auto_20220329_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='difficluty',
            field=models.CharField(choices=[('easy', 'easy'), ('medium', 'medium'), ('hard', 'hard')], default='easy', max_length=6),
        ),
        migrations.AddField(
            model_name='quiz',
            name='required_score_to_pass',
            field=models.IntegerField(default=50, help_text='required score in %'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='time',
            field=models.IntegerField(default=2, help_text='duration of the quiz in minutes'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='topic',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='quizzes.question'),
        ),
    ]