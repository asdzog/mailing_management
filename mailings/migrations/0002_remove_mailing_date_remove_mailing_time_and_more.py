# Generated by Django 4.2.7 on 2024-03-26 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mailings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailing',
            name='date',
        ),
        migrations.RemoveField(
            model_name='mailing',
            name='time',
        ),
        migrations.AddField(
            model_name='mailing',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата окончания рассылки'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата начала рассылки'),
        ),
        migrations.AddField(
            model_name='message',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]
