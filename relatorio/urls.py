from django.urls import path
from .views import GeneratePDFGeral, GeneratePDFReceitas, GeneratePDFDespesas

app_name = 'relatorio'

urlpatterns = [
    path('relatorio-geral/', GeneratePDFGeral.as_view(), name='gerar_relatorio_geral'),
    path('relatorio-receitas/', GeneratePDFReceitas.as_view(), name='gerar_relatorio_receitas'),
    path('relatorio-despesas/', GeneratePDFDespesas.as_view(), name='gerar_relatorio_despesas'),
]