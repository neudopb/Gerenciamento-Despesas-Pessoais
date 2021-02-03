from django.contrib import admin
from .models import Gerenciador, Categoria, Receita, Despesa

admin.site.register(Gerenciador)
admin.site.register(Categoria)
admin.site.register(Receita)
admin.site.register(Despesa)

