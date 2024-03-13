from django.shortcuts import render
from django.views.generic import TemplateView

from mailings.models import Message, Mailing, MailingLog


# Create your views here.
class HomeView(TemplateView):
    model = Mailing
    template_name = 'mailings/base.html'
    extra_context = {
        'title': 'index'
    }
