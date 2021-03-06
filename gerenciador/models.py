from django.db import models
from django.db.models import Q
from django.db.models import Sum, Value as V
from django.db.models.functions import Coalesce

class Gerenciador(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_gerenciador")
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    receita_total = models.DecimalField(max_digits=10, decimal_places=2)
    despesa_total = models.DecimalField(max_digits=10, decimal_places=2)
    id_usuario = models.ForeignKey("accounts.Usuario", db_column='id_usuario', on_delete=models.CASCADE)

    def update_gerenciador(self):

        gerenc = Gerenciador.objects.get(id_usuario=self.request.user.id)
        rec_sum = Receita.objects.filter(Q(recebido=True) & Q(id_gerenciador=gerenc.id)).aggregate(rs=Coalesce(Sum('valor'), V(0)))['rs']
        desp_sum = Despesa.objects.filter(Q(pago=True) & Q(id_gerenciador=gerenc.id)).aggregate(ds=Coalesce(Sum('valor'),V(0)))['ds']
        saldo_ttl = rec_sum - desp_sum
        Gerenciador.objects.filter(id=gerenc.id).update(saldo=saldo_ttl, receita_total=rec_sum, despesa_total=desp_sum)

    def __str__(self):
        return '{}'.format(self.id)
    class Meta:
        db_table = "gerenciador"

class Categoria(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_categoria")
    nome = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.nome)

    class Meta:
        verbose_name_plural = "categorias"
        db_table = "categoria"

class Receita(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_receita")
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    recebido = models.BooleanField(default=False)
    data = models.DateField()
    descricao = models.TextField(null=True, blank=True)
    receita_fixa = models.BooleanField(default=False)
    fixa_ativa = models.BooleanField(default=False)
    id_gerenciador = models.ForeignKey(Gerenciador, db_column="id_gerenciador", on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(Categoria, db_column="id_categoria", on_delete=models.CASCADE)

    def  __str__(self):
        return '{}'.format(self.id)

    class Meta:
        verbose_name_plural = "receitas"
        db_table = "receita"

class Despesa(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_despesa")
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    pago = models.BooleanField(default=False)
    data = models.DateField()
    descricao = models.TextField(null=True, blank=True)
    despesa_fixa = models.BooleanField(default=False)
    fixa_ativa = models.BooleanField(default=False)
    id_gerenciador = models.ForeignKey(Gerenciador, db_column="id_gerenciador", on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(Categoria, db_column="id_categoria", on_delete=models.CASCADE)

    def  __str__(self):
        return '{}'.format(self.id)

    class Meta:
        verbose_name_plural = "despesas"
        db_table = "despesa"
