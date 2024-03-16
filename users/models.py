from django.contrib.auth.models import AbstractUser
from django.db import models
from clients.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE)
    email_verified = models.BooleanField(default=False, verbose_name='email подтвержден')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
