from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView

from mailings.forms import MailingForm, MessageForm
from mailings.models import Message, Mailing, MailingLog


# Create your views here.
class HomeView(TemplateView):
    model = Mailing
    template_name = 'mailings/home.html'
    extra_context = {
        'title': 'Главная страница сервиса рассылок'
    }


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
            new_mailing.save()

        return super().form_valid(form)


class MailingListView(ListView):
    model = Mailing
    extra_context = {
        'title': 'Рассылки'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_active=True)
        return queryset


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
