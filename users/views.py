import random

from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from config import settings
from users.froms import UserRegisterForm, UserProfileForm
from users.models import User
CHARS = '+-*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        token = ''
        for i in range(10):
            token += random.choice(CHARS)
        form.verified_pass = token
        user = form.save()
        user.token = token
        send_mail(
            subject='Верификация почты',
            message=f'Поздравляем с регистрацией на SkyStore \n'
                    f'Для подтверждения регистрации перейдите по ссылке: \n'
                    f'http://127.0.0.1:8080/users/confirm/{user.token} \n'
                    f'Если вы не причастны к регистрации игнорируйте это письмо.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def verify_view(request, token):
    code = request.GET.get('code')
    user = User.objects.get(token=code)
    print(User.objects.get(token=code))
    user.is_verified = True
    user.save()
    return render(request, 'users/verify.html')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

