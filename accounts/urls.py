from django.urls import path, include
from .views import LoginView, LogoutView, UserCreateView, PasswordResetView
from rest_framework import routers
from .api.viewsets import UsuarioViewSet
from django.views.generic import TemplateView

app_name = 'accounts'

router = routers.DefaultRouter()
router.register(r'-usuario', UsuarioViewSet)

urlpatterns = [
    #path('login/', LoginView.as_view(), name="my_login"),
    #path('logout/', LogoutView.as_view(), name="my_logout"),
    path('cadastrar/', UserCreateView.as_view(), name="cadastrar_usuario"),
    #path('password_reset/', PasswordResetView.as_view(), name="Password_reset"),
    path('api', include(router.urls)),
    path('perfil/', TemplateView.as_view(template_name="accounts/perfil.html")),

]