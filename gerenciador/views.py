from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Gerenciador, Categoria, Receita, Despesa
from .forms import GerenciadorForm, CategoriaForm, ReceitaForm, DespesaForm
from django.db.models import Q

#INDEX
@method_decorator(login_required, name='dispatch')
class IndexView(LoginRequiredMixin, ListView):
    template_name ='gerenciador/index.html'
    context_object_name = 'list_gerenciador'

    def get_queryset(self):
        gerenciador = Gerenciador.objects.get(id_usuario=self.request.user.id)
        return gerenciador

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gerenc = Gerenciador.objects.get(id_usuario=self.request.user.id)
        context['list_gerenciador'] = gerenc
        context['ttl_rec'] = Receita.objects.filter(Q(id_gerenciador=gerenc.id) & Q(recebido=False)).count()
        context['ttl_desp'] = Despesa.objects.filter(Q(id_gerenciador=gerenc.id) & Q(pago=False)).count()
        return context

#CRUD CATEGORIA

@method_decorator(login_required, name='dispatch')
class CategoriaCreate(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'gerenciador/categoria_create.html'
    success_url = reverse_lazy('gerenciador:listCategoria')

@method_decorator(login_required, name='dispatch')
class CategoriaUpdate(LoginRequiredMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
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
    form_class = GerenciadorForm
    template_name = 'gerenciador/gerenciador_create.html'
    success_url = reverse_lazy('gerenciador:listGerenciador')

@method_decorator(login_required, name='dispatch')
class GerenciadorUpdate(LoginRequiredMixin, UpdateView):
    model = Gerenciador
    form_class = GerenciadorForm
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
    form_class = ReceitaForm
    template_name = 'gerenciador/receita_create.html'
    success_url = 'gerenciador:index'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["id_gerenc"] = Gerenciador.objects.get(id_usuario=self.request.user.id)
        context["TipoCategoria"] = Categoria.objects.filter(tipo="Receitas")
        return context

    def form_valid(self, form):
        rec = form.save()
        gerenc = Gerenciador.objects.get(id_usuario=self.request.user.id)
        rec_ttl = rec.valor + gerenc.receita_total
        sald = rec.valor + gerenc.saldo
        Gerenciador.objects.filter(id=gerenc.id).update(saldo=sald, receita_total=rec_ttl)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(self.success_url)

@method_decorator(login_required, name='dispatch')
class ReceitaUpdate(LoginRequiredMixin, UpdateView):
    model = Receita
    form_class = ReceitaForm
    template_name = 'gerenciador/receita_update.html'
    success_url = reverse_lazy('gerenciador:listReceita')

@method_decorator(login_required, name='dispatch')
class ReceitaList(LoginRequiredMixin, ListView):
    model = Receita
    context_object_name = 'list_receita'
    template_name = 'gerenciador/receita_list.html'

    def get_queryset(self):
        gerenc = Gerenciador.objects.get(id_usuario=self.request.user.id)
        receitas = Receita.objects.filter(Q(receita_fixa=False) & Q(id_gerenciador=gerenc.id))
        return receitas

@method_decorator(login_required, name='dispatch')
class ReceitaListFixa(LoginRequiredMixin, ListView):
    model = Receita
    context_object_name = 'list_receita'
    template_name = 'gerenciador/receita_list_fixa.html'

    def get_queryset(self):
        gerenc = Gerenciador.objects.get(id_usuario=self.request.user.id)
        receitas = Receita.objects.filter(Q(receita_fixa=True) & Q(id_gerenciador=gerenc.id))
        return receitas

@method_decorator(login_required, name='dispatch')
class ReceitaDelete(LoginRequiredMixin, DeleteView):
    model = Receita
    template_name = 'gerenciador/receita_confirm_delete.html'
    success_url = reverse_lazy('gerenciador:listReceita')

#CRUD DESPESA

@method_decorator(login_required, name='dispatch')
class DespesaCreate(LoginRequiredMixin, CreateView):
    model = Despesa
    form_class = DespesaForm
    template_name = 'gerenciador/despesa_create.html'
    success_url = 'gerenciador:index'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_gerenc'] = Gerenciador.objects.get(id_usuario=self.request.user.id)
        context["TipoCategoria"] = Categoria.objects.filter(tipo="Despesas")
        return context

    def form_valid(self, form):
        desp = form.save()
        gerenc = Gerenciador.objects.get(id_usuario=self.request.user.id)
        desp_ttl = desp.valor + gerenc.despesa_total
        sald = gerenc.saldo - desp.valor
        Gerenciador.objects.filter(id=gerenc.id).update(saldo=sald, despesa_total=desp_ttl)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(self.success_url)

@method_decorator(login_required, name='dispatch')
class DespesaUpdate(LoginRequiredMixin, UpdateView):
    model = Despesa
    form_class = DespesaForm
    template_name = 'gerenciador/despesa_update.html'
    success_url = reverse_lazy('gerenciador:listDespesa')

@method_decorator(login_required, name='dispatch')
class DespesaList(LoginRequiredMixin, ListView):
    model = Despesa
    context_object_name = 'list_despesa'
    template_name = 'gerenciador/despesa_list.html'

    def get_queryset(self):
        gerenc = Gerenciador.objects.get(id_usuario=self.request.user.id)
        despesas = Despesa.objects.filter(Q(despesa_fixa=False) & Q(id_gerenciador=gerenc.id))
        return despesas

@method_decorator(login_required, name='dispatch')
class DespesaListFixa(LoginRequiredMixin, ListView):
    model = Despesa
    context_object_name = 'list_despesa'
    template_name = 'gerenciador/despesa_list_fixa.html'

    def get_queryset(self):
        gerenc = Gerenciador.objects.get(id_usuario=self.request.user.id)
        despesas = Despesa.objects.filter(Q(despesa_fixa=True) & Q(id_gerenciador=gerenc.id))
        return despesas

@method_decorator(login_required, name='dispatch')
class DespesaDelete(LoginRequiredMixin, DeleteView):
    model = Despesa
    template_name = 'gerenciador/despesa_confirm_delete.html'
    success_url = reverse_lazy('gerenciador:listDespesa')

@method_decorator(login_required, name='dispatch')
class Pendencias(LoginRequiredMixin, ListView):
    model = Despesa
    context_object_name = 'list_pendencias'
    template_name = 'gerenciador/pendencias_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gerenc = Gerenciador.objects.get(id_usuario=self.request.user.id)
        context['receitas'] = Receita.objects.filter(Q(receita_fixa=False) & Q(id_gerenciador=gerenc.id) & Q(recebido=False))
        context['receitas_fixas'] = Receita.objects.filter(Q(receita_fixa=True) & Q(id_gerenciador=gerenc.id) & Q(recebido=False))
        context['despesas'] = Despesa.objects.filter(Q(despesa_fixa=False) & Q(id_gerenciador=gerenc.id) & Q(pago=False))
        context['despesas_fixas'] = Despesa.objects.filter(Q(despesa_fixa=True) & Q(id_gerenciador=gerenc.id) & Q(pago=False))
        return context