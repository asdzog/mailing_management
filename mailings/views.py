from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView

from mailings.forms import MailingForm
from mailings.models import Message, Mailing, MailingLog


# Create your views here.
class HomeView(TemplateView):
    model = Mailing
    template_name = 'mailings/home.html'
    extra_context = {
        'title': 'index'
    }


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    extra_context = {
        'title': 'Создание рассылки'
    }


class MailingListView(ListView):
    pass


class MailingUpdateView(UpdateView):
    pass


class MailingDeleteView(DeleteView):
    pass


class MailingDetailView(DetailView):
    pass
