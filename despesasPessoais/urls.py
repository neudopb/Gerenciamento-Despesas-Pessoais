from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import urls
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='APIs do Sistema de Gerenciamento de Despesas Pessoais')

urlpatterns = [
    path('', include('gerenciador.urls', namespace='gerenciador')),
    path('', include('accounts.urls', namespace='accounts')),
    #path('account/', include('django.contrib.auth.urls')), #accounts
    path('', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', schema_view),
    path('admin/', admin.site.urls),
]
