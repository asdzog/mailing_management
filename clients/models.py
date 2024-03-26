from django.db import models

from django.conf import settings

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    """Client model"""
    email = models.EmailField(max_length=100, unique=True, verbose_name='Почта')
    full_name = models.CharField(verbose_name='ФИО')
    comment = models.TextField(**NULLABLE, verbose_name='Комментарий')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, verbose_name='чей клиент')

    def __str__(self):
        return f'{self.full_name} ({self.email})'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
