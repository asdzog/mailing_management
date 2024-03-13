from django.urls import path

from mailings.views import HomeView

app_name = 'mailings'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]

