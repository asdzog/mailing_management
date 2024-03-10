from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    """Client model"""
    email = models.EmailField(max_length=100, unique=True, verbose_name='Почта')
    full_name = models.CharField(verbose_name='ФИО')
    comment = models.TextField(**NULLABLE, verbose_name='Комментарий')

    def __str__(self):
        return f'{self.full_name} ({self.email})'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
