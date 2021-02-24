from rest_framework import viewsets
from ..models import Gerenciador, Categoria, Receita, Despesa
from .serializers import CategoriaSerializer, GerenciadorSerializer, ReceitaSerializer, DespesaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    """API para CATEGORIA"""
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class GerenciadorViewSet(viewsets.ModelViewSet):
    """API para GERENCIADOR"""
    queryset = Gerenciador.objects.all()
    serializer_class = GerenciadorSerializer

class ReceitaViewSet(viewsets.ModelViewSet):
    """API para RECEITA"""
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer

class DespesaViewSet(viewsets.ModelViewSet):
    """API para DESPESA"""
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer