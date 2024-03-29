from django.core.management.base import BaseCommand
from mailings.models import Mailing


class Command(BaseCommand):
    help = 'List all mailings'

    def handle(self, *args, **options):
        mailings = Mailing.objects.all()
        if mailings:
            self.stdout.write("Список рассылок:")
            for mailing in mailings:
                self.stdout.write(f"- {mailing.title} (ID {mailing.id})")
        else:
            self.stdout.write("Рассылки не найдены")
