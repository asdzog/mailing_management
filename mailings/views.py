from django.shortcuts import render
from django.utils.text import slugify
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

    def form_valid(self, form):
        if form.is_valid():
            new_mailing = form.save()
            new_mailing.slug = slugify(new_mailing.title)
            new_mailing.save()

        return super().form_valid(form)


class MailingListView(ListView):
    model = Mailing

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_active=True)
        return queryset


class MailingUpdateView(UpdateView):
    pass


class MailingDeleteView(DeleteView):
    pass


class MailingDetailView(DetailView):
    pass
