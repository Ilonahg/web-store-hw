from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings

from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import CustomUser

class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        send_mail(
            subject='Добро пожаловать!',
            message='Спасибо за регистрацию на нашем сайте.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[form.cleaned_data['email']],
            fail_silently=True,
        )
        return response

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'users/login.html'
