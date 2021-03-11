from django.urls import path, include
from .views import UserCreateView, UserUpdateView
from rest_framework import routers
from .api.viewsets import UsuarioViewSet
from django.views.generic import TemplateView

app_name = 'accounts'

router = routers.DefaultRouter()
router.register(r'-usuario', UsuarioViewSet)

urlpatterns = [
    path('cadastrar/', UserCreateView.as_view(), name="cadastrar_usuario"),
    path('api', include(router.urls)),
    path('update_user/<int:pk>/', UserUpdateView.as_view(), name="update_usuario"),
]