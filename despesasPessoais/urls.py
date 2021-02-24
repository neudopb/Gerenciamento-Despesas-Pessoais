from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import urls
from gerenciador.views import CategoriaViewSet, GerenciadorViewSet, ReceitaViewSet, DespesaViewSet
from accounts.views import UsuarioViewSet
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='APIs do Sistema de Gerenciamento de Despesas Pessoais')

router = routers.DefaultRouter()
router.register(r'api-usuario', UsuarioViewSet)
router.register(r'api-categoria', CategoriaViewSet)
router.register(r'api-gerenciador', GerenciadorViewSet)
router.register(r'api-receita', ReceitaViewSet)
router.register(r'api-despesa', DespesaViewSet)

urlpatterns = [
    path('', include('gerenciador.urls', namespace='gerenciador')),
    path('', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('swagger/', schema_view),
    path('admin/', admin.site.urls),
]
