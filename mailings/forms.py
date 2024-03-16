from django.forms import ModelForm

from clients.forms import StyleFormMixin
from mailings.models import Message, Mailing, MailingLog


class MailingForm(StyleFormMixin, ModelForm):

    class Meta:
        model = Mailing
        fields = '__all__'


class MessageForm(StyleFormMixin, ModelForm):

    class Meta:
        model = Message
        fields = '__all__'


class MailingLogForm(StyleFormMixin, ModelForm):

    class Meta:
        model = MailingLog
        fields = '__all__'
