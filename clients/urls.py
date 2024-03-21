from django.urls import path


from clients.views import ClientCreateView, ClientListView, ClientUpdateView, ClientDeleteView, ClientDetailView

app_name = 'clients'

urlpatterns = [

    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('client_detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
]
