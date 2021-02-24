from rest_framework import serializers
from ..models import Categoria, Gerenciador, Receita, Despesa

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class GerenciadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gerenciador
        fields = '__all__'

class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = '__all__'

class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = '__all__'