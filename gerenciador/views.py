from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Gerenciador, Categoria, Receita, Despesa
from .forms import GerenciadorForm, CategoriaForm, ReceitaForm, DespesaForm

@method_decorator(login_required, name='dispatch')
class IndexView(LoginRequiredMixin, TemplateView):
    template_name ='gerenciador/index.html'

#CRUD CATEGORIA

@method_decorator(login_required, name='dispatch')
class CategoriaCreate(LoginRequiredMixin, CreateView):
    model = Categoria
    fields = '__all__'
    template_name = 'gerenciador/categoria_create.html'
    success_url = reverse_lazy('gerenciador:listCategoria')

@method_decorator(login_required, name='dispatch')
class CategoriaUpdate(LoginRequiredMixin, UpdateView):
    model = Categoria
    fields = '__all__'
    template_name = 'gerenciador/categoria_update.html'
    success_url = reverse_lazy('gerenciador:listCategoria')

@method_decorator(login_required, name='dispatch')
class CategoriaList(LoginRequiredMixin, ListView):
    model = Categoria
    context_object_name = 'list_categoria'
    template_name = 'gerenciador/categoria_list.html'

@method_decorator(login_required, name='dispatch')
class CategoriaDelete(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'gerenciador/categoria_confirm_delete.html'
    success_url = reverse_lazy('gerenciador:listCategoria')

#CRUD GERENCIADOR

@method_decorator(login_required, name='dispatch')
class GerenciadorCreate(LoginRequiredMixin, CreateView):
    model = Gerenciador
    fields = '__all__'
    template_name = 'gerenciador/gerenciador_create.html'
    success_url = reverse_lazy('gerenciador:listGerenciador')

@method_decorator(login_required, name='dispatch')
class GerenciadorUpdate(LoginRequiredMixin, UpdateView):
    model = Gerenciador
    fields = '__all__'
    template_name = 'gerenciador/gerenciador_update.html'
    success_url = reverse_lazy('gerenciador:listGerenciador')

@method_decorator(login_required, name='dispatch')
class GerenciadorList(LoginRequiredMixin, ListView):
    model = Gerenciador
    context_object_name = 'list_gerenciador'
    template_name = 'gerenciador/gerenciador_list.html'

@method_decorator(login_required, name='dispatch')
class GerenciadorDelete(LoginRequiredMixin, DeleteView):
    model = Gerenciador
    template_name = 'gerenciador/gerenciador_confirm_delete.html'
    success_url = reverse_lazy('gerenciador:listGerenciador')

#CRUD RECEITA

@method_decorator(login_required, name='dispatch')
class ReceitaCreate(LoginRequiredMixin, CreateView):
    model = Receita
    fields = '__all__'
    template_name = 'gerenciador/receita_create.html'
    success_url = reverse_lazy('gerenciador:listReceita')

@method_decorator(login_required, name='dispatch')
class ReceitaUpdate(LoginRequiredMixin, UpdateView):
    model = Receita
    fields = '__all__'
    template_name = 'gerenciador/receita_update.html'
    success_url = reverse_lazy('gerenciador:listReceita')

@method_decorator(login_required, name='dispatch')
class ReceitaList(LoginRequiredMixin, ListView):
    model = Receita
    context_object_name = 'list_receita'
    template_name = 'gerenciador/receita_list.html'

@method_decorator(login_required, name='dispatch')
class ReceitaDelete(LoginRequiredMixin, DeleteView):
    model = Receita
    template_name = 'gerenciador/receita_confirm_delete.html'
    success_url = reverse_lazy('gerenciador:listReceita')

#CRUD DESPESA

@method_decorator(login_required, name='dispatch')
class DespesaCreate(LoginRequiredMixin, CreateView):
    model = Despesa
    fields = '__all__'
    template_name = 'gerenciador/despesa_create.html'
    success_url = reverse_lazy('gerenciador:listDespesa')

@method_decorator(login_required, name='dispatch')
class DespesaUpdate(LoginRequiredMixin, UpdateView):
    model = Despesa
    fields = '__all__'
    template_name = 'gerenciador/despesa_update.html'
    success_url = reverse_lazy('gerenciador:listDespesa')

@method_decorator(login_required, name='dispatch')
class DespesaList(LoginRequiredMixin, ListView):
    model = Despesa
    context_object_name = 'list_despesa'
    template_name = 'gerenciador/despesa_list.html'

@method_decorator(login_required, name='dispatch')
class DespesaDelete(LoginRequiredMixin, DeleteView):
    model = Despesa
    template_name = 'gerenciador/despesa_confirm_delete.html'
    success_url = reverse_lazy('gerenciador:listDespesa')