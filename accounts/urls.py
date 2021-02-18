from django.urls import path
from .views import LoginView, LogoutView, UserCreateView, ResetPassword

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('cadastrar/', UserCreateView.as_view(), name="cadastrar_usuario"),
    path('password/', ResetPassword.as_view(), name="mudar_senha"),
]