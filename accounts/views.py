from django.contrib import messages
from django.urls import reverse_lazy
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LogoutView
from .forms import UsuarioRegisterForm
from .models import Usuario
from gerenciador.models import Gerenciador
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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

@method_decorator(login_required, name='dispatch')
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    fields = ('first_name', 'last_name')
    template_name = 'accounts/update_user.html'
    success_url = reverse_lazy('gerenciador:index')