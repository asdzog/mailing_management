import os
from django.core.mail import send_mail
from mailings.models import Mailing, Message, MailingLog


def send_mailing_emails(mailing: Mailing):
    """ Function for sending email and writing logs """

    try:
        for client in mailing.clients.all():
            messages = Message.objects.filter(mailing=mailing)
            for message in messages:
                send_mail(
                    subject=message.subject,
                    message=message.body,
                    from_email=os.getenv('EMAIL_HOST_USER'),
                    recipient_list=[client.email],
                    fail_silently=False,
                )

                # Create an entry in the mailing log
                MailingLog.objects.create(
                    status='SENT',
                    response='Email successfully sent',
                    mailing=mailing
                )
        return True
    except Exception as e:
        # If an error occurs, create an entry in the mailing log with indicating the error
        MailingLog.objects.create(
            status='FAILED',
            response=str(e),
            mailing=mailing
        )
        return False
