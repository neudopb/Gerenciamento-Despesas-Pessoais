from django.forms import ModelForm
from .models import Gerenciador, Categoria, Receita, Despesa

class GerenciadorForm(ModelForm):
    class Meta:
        model = Gerenciador
        fields = ['saldo', 'receita_total', 'despesa_total', 'id_usuario']

    def save(self, commit=True):
        gerenciador = super(GerenciadorForm, self).save()
        gerenciador.id_usuario = self.cleaned_data['id_usuario']

        if commit:
            gerenciador.save()
        return gerenciador

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'tipo']

class ReceitaForm(ModelForm):
    class Meta:
        model = Receita
        fields = ['valor', 'recebido', 'data', 'descricao', 'receita_fixa', 'fixa_ativa', 'id_gerenciador', 'id_categoria']

    def save(self, commit=True):
        receita = super(ReceitaForm, self).save()
        receita.id_categoria = self.cleaned_data['id_categoria']
        receita.id_gerenciador = self.cleaned_data['id_gerenciador']

        if commit:
            receita.save()
        return receita

class DespesaForm(ModelForm):
    class Meta:
        model = Despesa
        fields = ['valor', 'pago', 'data', 'descricao', 'despesa_fixa', 'fixa_ativa', 'id_gerenciador', 'id_categoria']

    def save(self, commit=True):
        despesa = super(DespesaForm, self).save()
        despesa.id_categoria = self.cleaned_data['id_categoria']
        despesa.id_gerenciador = self.cleaned_data['id_gerenciador']

        if commit:
            despesa.save()
        return despesa