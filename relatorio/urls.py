from django.urls import path
from .views import GeneratePdf

app_name = 'relatorio'

urlpatterns = [
    path('relatorio/', GeneratePdf.as_view(), name='gerar_relatorio'),
]