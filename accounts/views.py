from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.urls import reverse_lazy
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UsuarioRegisterForm
from .models import Usuario
from gerenciador.models import Gerenciador
from .serializers import UsuarioSerializer
from rest_framework import viewsets

#API
class UsuarioViewSet(viewsets.ModelViewSet):
    """API para USUARIO"""
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class LoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = settings.LOGIN_REDIRECT_URL


class LogoutView(LogoutView):
    template_name = 'index'

class UserCreateView(CreateView):
    model = Usuario
    success_url = 'accounts:login'
    template_name = 'accounts/create.html'
    form_class = UsuarioRegisterForm

    def form_valid(self, form):
        self.usuario = form.save()
        Gerenciador.objects.create(saldo=0, receita_total=0, despesa_total=0, id_usuario=self.usuario)

        send_mail(
            'Cliente Cadastrado',
            '%s, você foi cadastrado com sucesso.' % self.usuario.first_name,
            'despess21@gmail.com',
            [self.usuario.email],
            fail_silently=False,
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Usuário cadastrado com sucesso!')
        return reverse_lazy(self.success_url)

class PasswordResetView(TemplateView):
    template_name = "accounts/forgot-password.html"