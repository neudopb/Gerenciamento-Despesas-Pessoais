from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginView, LogoutView, UserCreateView, PasswordResetView

app_name = 'accounts'

urlpatterns = [
    #path('login/', LoginView.as_view(), name="my_login"),
    #path('logout/', LogoutView.as_view(), name="my_logout"),
    path('cadastrar/', UserCreateView.as_view(), name="cadastrar_usuario"),
    #path('password_reset/', PasswordResetView.as_view(), name="Password_reset"),
]