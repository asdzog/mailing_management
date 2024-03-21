from django.urls import path

from mailings.views import HomeView, MailingCreateView, MailingListView, MailingUpdateView, MailingDeleteView, \
    MailingDetailView, MessageCreateView, MessageDetailView, MessageListView, MessageUpdateView, MessageDeleteView

app_name = 'mailings'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('mailing_create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing_detail/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing_list/', MailingListView.as_view(), name='mailing_list'),
    path('mailing_update/<int:pk>/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing_delete/<int:pk>/', MailingDeleteView.as_view(), name='mailing_delete'),

    path('message_create/', MessageCreateView.as_view(), name='message_create'),
    path('message_detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message_list/', MessageListView.as_view(), name='message_list'),
    path('message_update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),

]
