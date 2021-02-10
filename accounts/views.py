from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UsuarioRegisterForm
from .models import Usuario

class LoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = settings.LOGIN_REDIRECT_URL


class LogoutView(LogoutView):
    template_name = 'index'

class UserCreateView(CreateView):
    model = Usuario
    success_url = 'login'
    template_name = 'accounts/create.html'
    form_class = UsuarioRegisterForm

    def get_success_url(self):
        messages.success(self.request, 'Usuário cadastrado com sucesso!')
        return reverse(self.success_url)