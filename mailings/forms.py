from django.forms import ModelForm

from clients.forms import StyleFormMixin
from mailings.models import Message, Mailing, MailingLog


class MailingForm(StyleFormMixin, ModelForm):

    class Meta:
        model = Mailing
        exclude = ('owner',)


class MessageForm(StyleFormMixin, ModelForm):

    class Meta:
        model = Message
        exclude = ('owner',)


class MailingLogForm(StyleFormMixin, ModelForm):

    class Meta:
        model = MailingLog
        exclude = ('owner',)
