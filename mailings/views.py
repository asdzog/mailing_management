from random import random, shuffle
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView

from blog.models import Post
from clients.models import Client
from mailings.forms import MailingForm, MessageForm
from mailings.models import Message, Mailing, MailingLog
from mailings.utils import get_cached_all_mailings, get_cached_active_mailings


# Create your views here.
class HomeView(TemplateView):
    model = Mailing
    template_name = 'mailings/home.html'
    extra_context = {
        'title': 'Главная страница сервиса рассылок'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['mailings_count'] = get_cached_all_mailings()
        context_data['active_mailings_count'] = get_cached_active_mailings()
        blog_list = list(Post.objects.all())
        shuffle(blog_list)
        context_data['blog_list'] = blog_list[:3]
        context_data['clients_count'] = len(Client.objects.all())
        return context_data


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailings:mailing_list')
    extra_context = {
        'title': 'Создание рассылки'
    }

    def form_valid(self, form):
        if form.is_valid():
            new_mailing = form.save()
            new_mailing.owner = self.request.user
            new_mailing.save()

        return super().form_valid(form)


class MailingListView(ListView):
    model = Mailing
    extra_context = {
        'title': 'Рассылки'
    }


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = '__all__'
    success_url = reverse_lazy('mailings:mailing_list')

    def form_valid(self, form):
        if form.is_valid():
            new_mailing = form.save()
            new_mailing.save()

        return super().form_valid(form)


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailings:mailing_list')


class MailingDetailView(DetailView):
    model = Mailing


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailings:message_list')
    extra_context = {
        'title': 'Создание письма для рассылки'
    }

    def form_valid(self, form):
        if form.is_valid():
            new_email = form.save()
            new_email.owner = self.request.user
            new_email.save()

        return super().form_valid(form)


class MessageListView(ListView):
    model = Message
    extra_context = {
        'title': 'Письма'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        return queryset


class MessageUpdateView(UpdateView):
    model = Message
    fields = '__all__'
    success_url = reverse_lazy('mailings:message_list')

    def form_valid(self, form):
        if form.is_valid():
            new_email = form.save()
            new_email.save()

        return super().form_valid(form)


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailings:message_list')


class MessageDetailView(DetailView):
    model = Message


class MailingLogListView(ListView):
    model = MailingLog
    extra_context = {
        'title': 'Логи рассылок'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        return queryset
