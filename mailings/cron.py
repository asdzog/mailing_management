from calendar import calendar
from datetime import timedelta, datetime
from smtplib import SMTPException
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail

from mailings.models import Mailing, MailingLog


def get_mailings():
    active_mailings = Mailing.objects.filter(is_active=True)
    current_time = timezone.localtime(timezone.now())
    now = current_time.strftime('%Y-%m-%d %H:%M')
    for mailing in active_mailings:
        # проверка вхождения времени рассылки в нужный интервал
        if mailing.start_date >= current_time:
            mailing.status = "создана"
            mailing.save()
        elif mailing.end_date <= current_time:
            mailing.status = "закончена"
            mailing.save()
        elif mailing.start_date.strftime('%Y-%m-%d %H:%M') <= now <= mailing.end_date.strftime('%Y-%m-%d %H:%M'):
            mailing.status = "начата"
            mailing.save()
            # определение периодичности рассылки
            next_sending = mailing.next_date.strftime('%Y-%m-%d %H:%M')
            if next_sending <= now:
                if mailing.period == "ежедневно":
                    mailing.next_date = current_time + timedelta(days=1)
                    mailing.save()
                elif mailing.period == "еженедельно":
                    mailing.next_date = current_time + timedelta(days=7)
                    mailing.save()
                elif mailing.period == "ежемесячно":
                    today = datetime.today()
                    days = calendar.monthrange(today.year, today.month)[1]
                    mailing.next_date = current_time + timedelta(days=days)
                    mailing.save()
                if mailing.next_date > mailing.end_date:
                    mailing.status = "закончена"
                    mailing.save()

                status = True
                error_message = ''
                try:
                    send_mail(
                        subject=mailing.message.subject,
                        message=mailing.message.body,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[client.email for client in mailing.clients.all()],
                        fail_silently=False
                    )
                    status = True
                    error_message = 'OK'
                except SMTPException as error:
                    status = False
                    if 'authentication failed' in str(error):
                        error_message = 'Ошибка аутентификации в почтовом сервисе'
                    elif 'suspicion of SPAM' in str(error):
                        error_message = 'Подозрение на спам, сервис отклонил письмо'
                    else:
                        error_message = error
                finally:
                    log = MailingLog.objects.create(
                        status=status,
                        response=error_message,
                        mailing=mailing,
                        owner=mailing.owner
                    )
                    log.save()
            elif mailing.next_date >= mailing.end_date:
                mailing.status = "закончена"
                mailing.save()
