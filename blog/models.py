from django.db import models

from clients.models import NULLABLE


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField(verbose_name='Содержание', **NULLABLE)
    preview = models.ImageField(upload_to='blog/', verbose_name='Превью')
    views_count = models.IntegerField(verbose_name='Просмотры', default=0)
    date_published = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_active = models.BooleanField(verbose_name='Активно', default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
