from django.db import models

class Gerenciador(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_gerenciador")
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    receita_total = models.DecimalField(max_digits=10, decimal_places=2)
    despesa_total = models.DecimalField(max_digits=10, decimal_places=2)
    id_usuario = models.ForeignKey("accounts.CustomUsuario", on_delete=models.CASCADE)

    def __str__(self):
        return self.id

    class Meta:
        db_table = "gerenciador"

class Categoria(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_categoria")
    nome = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

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
    id_gerenciador = models.ForeignKey(Gerenciador, on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def  __str__(self):
        return self.id + " - " + self.valor

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
    id_gerenciador = models.ForeignKey(Gerenciador, on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def  __str__(self):
        return self.id + " - " + self.valor

    class Meta:
        verbose_name_plural = "despesas"
        db_table = "despesa"
