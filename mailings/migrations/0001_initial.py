# Generated by Django 4.2.7 on 2024-03-13 16:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата')),
                ('time', models.TimeField(auto_now_add=True, verbose_name='Время')),
                ('period', models.CharField(choices=[('разовая', 'разовая'), ('ежедневно', 'ежедневно'), ('еженедельно', 'еженедельно'), ('ежемесячно', 'ежемесячно')], default='еженедельно', max_length=30, verbose_name='Период')),
                ('status', models.CharField(choices=[('создана', 'создана'), ('начата', 'начата'), ('закончена', 'закончена')], default='создана', max_length=10, verbose_name='Статус')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активна')),
                ('clients', models.ManyToManyField(to='clients.client', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=150, verbose_name='Тема')),
                ('body', models.TextField(verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Письмо',
                'verbose_name_plural': 'Письма',
            },
        ),
        migrations.CreateModel(
            name='MailingLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')),
                ('status', models.CharField(choices=[('SENT', 'sent'), ('FAILED', 'failed'), ('PENDING', 'pending')], max_length=50, verbose_name='Статус')),
                ('response', models.TextField(max_length=200, verbose_name='Ответ сервера')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailings.mailing', verbose_name='Рассылка')),
            ],
            options={
                'verbose_name': 'Лог',
                'verbose_name_plural': 'Логи',
            },
        ),
        migrations.AddField(
            model_name='mailing',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailings.message', verbose_name='Письмо'),
        ),
    ]
