from django import forms

from clients.models import Client


class StyleFormMixin:
    """ Mixin with from style """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(forms.ModelForm):

    last_name = forms.CharField(max_length='50', verbose_name='Фамилия')
    first_name = forms.CharField(max_length='50', verbose_name='Имя')
    middle_name = forms.CharField(max_length='50', verbose_name='Отчество')

    def clean(self):
        self.instance.full_name = '{last_name} {first_name} {middle_name}'.format(**self.cleaned_data)
        return self.cleaned_data

    class Meta:
        model = Client
        fields = '__all__'
