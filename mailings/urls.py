from django.urls import path

from mailings.views import HomeView, MailingCreateView, MailingListView, MailingUpdateView, MailingDeleteView, \
    MailingDetailView

app_name = 'mailings'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('mailing_create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing_detail/', MailingDetailView.as_view(), name='mailing_create'),
    path('mailing_list/', MailingListView.as_view(), name='mailing_list'),
    path('mailing_update/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing_delete/', MailingDeleteView.as_view(), name='mailing_delete'),
]
