from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import CreateView, TemplateView

from users.forms import UserRegisterForm
from users.models import User


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('mailings:home')


class UserLogoutView(LogoutView):
    model = User
    success_url = reverse_lazy('users:login')


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_user = form.save()
        new_user.save()
        token = default_token_generator.make_token(new_user)
        uid = urlsafe_base64_encode(force_bytes(new_user.pk))
        activation_url = reverse_lazy('users:confirm_email', kwargs={'uidb64': uid, 'token': token})
        current_site = '127.0.0.1:8000'
        send_mail(
            subject='Поздравляем с регистрацией!',
            message='Вы зарегистрировались на сайте сервиса рассылок.'
                    'Для подтверждения почтового адреса пройдите по следующей ссылке:\n'
                    f'http://{current_site}{activation_url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )

        return redirect('users:confirm_register')


class EmailConfirmView(TemplateView):
    template_name = 'users/confirm_register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Verify code sent'
        return context


class UserConfirmEmailView(View):

    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.email_verified = True
            user.save()
            login(request, user)
            return redirect('users:succeeded_register')
        else:
            return redirect('users:failed_register')


class RegisterFailView(View):
    template_name = 'users/failed_register.html'


class RegisterSuccessView(TemplateView):
    template_name = 'users/succeeded_register.html'


def generate_new_psw(request):
    new_password = User.objects.make_random_password()
    send_mail(
        subject='Вы успешно сменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return render(request, 'users/password_changed.html')
