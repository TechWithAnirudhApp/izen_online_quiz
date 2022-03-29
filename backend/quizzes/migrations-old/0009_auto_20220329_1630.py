# Generated by Django 3.1 on 2022-03-29 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quizzes', '0008_auto_20220329_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='name',
        ),
        migrations.AddField(
            model_name='result',
            name='user',
            field=models.ForeignKey(default='User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
