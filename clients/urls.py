from django.urls import path

from clients.apps import ClientsConfig
from clients.views import ClientCreateView, ClientListView, ClientUpdateView


app_name = 'clients'

urlpatterns = [

    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('client_update/', ClientUpdateView.as_view(), name='client_update'),
]
