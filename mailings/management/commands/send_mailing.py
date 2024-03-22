from django.core.management.base import BaseCommand
from mailings.models import Mailing
from mailings.services import send_mailing_emails
from django_crontab import crontab


class Command(BaseCommand):
    help = 'Send mailing emails'

    def handle(self, *args, **options):
        # send mailings from console by requesting mailing ID
        mailing_id = input("Введите ID рассылки: ")
        try:
            mailing = Mailing.objects.get(pk=int(mailing_id), is_active=True)
            success = send_mailing_emails(mailing)
            if success:
                self.stdout.write(self.style.SUCCESS('Рассылка успешно отправлена'))
            else:
                self.stderr.write(self.style.ERROR('Ошибка при отправке рассылки. Подробности см. в лог-файле'))
                # Вывод содержимого лог-файла для получения подробностей об ошибке
                with open('mailing_log.txt', 'r') as log_file:
                    print(log_file.read())
        except Mailing.DoesNotExist:
            self.stderr.write(self.style.ERROR('Рассылка с указанным ID не найдена'))
        except ValueError:
            self.stderr.write(self.style.ERROR('Некорректный ID рассылки'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Произошла ошибка: {e}'))

        # send periodic mailings
        periodic_mailings = Mailing.objects.filter(
            period__in=['ежедневно', 'еженедельно',
                        'ежемесячно'], is_active=True)
        for mailing in periodic_mailings:
            # checking periodicity and setting schedule for sending  mailings
            if mailing.period == 'ежедневно':
                crontab.every().day.do(send_mailing, mailing.id)
            elif mailing.period == 'еженедельно':
                crontab.every().week.do(send_mailing, mailing.id)
            elif mailing.period == 'ежемесячно':
                crontab.every().month.do(send_mailing, mailing.id)


def send_mailing(mailing_id):
    pass

