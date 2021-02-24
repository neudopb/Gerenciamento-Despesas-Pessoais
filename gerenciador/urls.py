from django.urls import path, include
from rest_framework import routers
from .views import IndexView
from .views import CategoriaCreate, CategoriaList, CategoriaUpdate, CategoriaDelete
from .views import GerenciadorCreate, GerenciadorList, GerenciadorUpdate, GerenciadorDelete
from .views import ReceitaCreate, ReceitaList, DespesaListFixa, ReceitaListFixa, ReceitaUpdate, ReceitaDelete
from .views import DespesaCreate, DespesaList, DespesaUpdate, DespesaDelete
from .api.viewsets import CategoriaViewSet, GerenciadorViewSet, ReceitaViewSet, DespesaViewSet

app_name = 'gerenciador'

router = routers.DefaultRouter()
router.register(r'api-categoria', CategoriaViewSet)
router.register(r'api-gerenciador', GerenciadorViewSet)
router.register(r'api-receita', ReceitaViewSet)
router.register(r'api-despesa', DespesaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', IndexView.as_view(), name='index'),
    path('categoria/create', CategoriaCreate.as_view(), name='createCategoria'),
    path('categoria/list', CategoriaList.as_view(), name='listCategoria'),
    path('categoria/update/<int:pk>/', CategoriaUpdate.as_view(), name='updateCategoria'),
    path('categoria/delete/<int:pk>/', CategoriaDelete.as_view(), name='deleteCategoria'),

    path('gerenciador/create', GerenciadorCreate.as_view(), name='createGerenciador'),
    path('gerenciador/list', GerenciadorList.as_view(), name='listGerenciador'),
    path('gerenciador/update/<int:pk>/', GerenciadorUpdate.as_view(), name='updateGerenciador'),
    path('gerenciador/delete/<int:pk>/', GerenciadorDelete.as_view(), name='deleteGerenciador'),

    path('receita/create', ReceitaCreate.as_view(), name='createReceita'),
    path('receita/list', ReceitaList.as_view(), name='listReceita'),
    path('receita/listfixa', ReceitaListFixa.as_view(), name='listFixaReceita'),
    path('receita/update/<int:pk>/', ReceitaUpdate.as_view(), name='updateReceita'),
    path('receita/delete/<int:pk>/', ReceitaDelete.as_view(), name='deleteReceita'),

    path('despesa/create', DespesaCreate.as_view(), name='createDespesa'),
    path('despesa/list', DespesaList.as_view(), name='listDespesa'),
    path('despesa/listfixa', DespesaListFixa.as_view(), name='listFixaDespesa'),
    path('despesa/update/<int:pk>/', DespesaUpdate.as_view(), name='updateDespesa'),
    path('despesa/delete/<int:pk>/', DespesaDelete.as_view(), name='deleteDespesa'),
]
