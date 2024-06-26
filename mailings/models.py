from django.conf import settings
from django.db import models
from django.utils import timezone
from clients.models import Client, NULLABLE


class Message(models.Model):

    subject = models.CharField(max_length=150, verbose_name='Тема')
    body = models.TextField(verbose_name="Сообщение")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return f'{self.subject}'

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'


class Mailing(models.Model):

    PERIOD_CHOICES = [
        ('ежедневно', 'ежедневно'),
        ('еженедельно', 'еженедельно'),
        ('ежемесячно', 'ежемесячно'),
    ]

    STATUS_CHOICES = [
        ('создана', 'создана'),
        ('начата', 'начата'),
        ('закончена', 'закончена')
    ]

    title = models.CharField(max_length=50, verbose_name='Название')
    start_date = models.DateTimeField(default=timezone.now, verbose_name='Дата начала рассылки')
    end_date = models.DateTimeField(default=timezone.now, verbose_name='Дата окончания рассылки')
    next_date = models.DateTimeField(**NULLABLE, verbose_name='Дата следующей рассылки')
    period = models.CharField(max_length=30, verbose_name='Период', choices=PERIOD_CHOICES, default='еженедельно')
    status = models.CharField(max_length=10, verbose_name='Статус', choices=STATUS_CHOICES, default='создана')
    clients = models.ManyToManyField(Client, verbose_name='Клиент')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Письмо')

    is_active = models.BooleanField(default=True, verbose_name='Активна')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, verbose_name='Владелец')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class MailingLog(models.Model):

    STATUS_CHOICES = [
        ('SENT', 'sent'),
        ('FAILED', 'failed'),
        ('PENDING', 'pending')
    ]

    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name='Статус')
    response = models.TextField(max_length=200, verbose_name='Ответ сервера')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, **NULLABLE, on_delete=models.SET_NULL, verbose_name='Владелец')

    def __str__(self):
        return f'Отправка {self.datetime}: {self.status}'

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
