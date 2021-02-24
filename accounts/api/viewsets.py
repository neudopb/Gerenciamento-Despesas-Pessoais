from rest_framework import viewsets
from ..models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    """API para USUARIO"""
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer