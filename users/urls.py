from django.urls import path

from users.apps import UsersConfig
from users.views import UserLoginView, RegisterView, UserConfirmEmailView, RegisterFailView, RegisterSuccessView, \
    UserLogoutView, EmailConfirmView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm_register/', EmailConfirmView.as_view(), name='confirm_register'),
    path('confirm_email/<str:uidb64>/<str:token>/', UserConfirmEmailView.as_view(), name='confirm_email'),
    path('failed_register/', RegisterFailView.as_view(), name='failed_register'),
    path('succeeded_register/', RegisterSuccessView.as_view(), name='succeeded_register'),

]
