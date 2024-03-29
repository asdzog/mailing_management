from django.core.management import BaseCommand
from django.conf import settings
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email=settings.ADM_EMAIL,
            first_name='admin',
            last_name='user_admin',
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )

        user.set_password(settings.ADM_PSW)
        user.save()
