from django import forms

from clients.models import Client


class StyleFormMixin:
    """ Mixin with from style """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        exclude = ('owner',)
