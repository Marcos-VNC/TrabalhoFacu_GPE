from django.db import models


class Endereco(models.Model):
    cep = models.CharField(max_length=50)
    numero = models.IntegerField()
    rua = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)
    def __str__(self):
        return self.id

class Fornecedor(models.Model):
    nome = models.CharField(max_length=50)
    cnpj = models.IntegerField()
    endereco = models.ForeignKey(Endereco, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.id

class Produto(models.Model):
    equipamento = models.CharField(max_length=255, verbose_name="Nome do Equipamento")
    ca = models.CharField(max_length=20, verbose_name="Número do CA")
    dataDeValidade = models.DateField(verbose_name="Data de Validade")
    situacao = models.CharField(
        max_length=100, verbose_name="Situação (Aprovado ou Vencido)"
    )
    quantidade = models.PositiveIntegerField(
        default=0, verbose_name="Quantidade em Estoque"
    )
    aprovadoPara = models.CharField(
        max_length=255, verbose_name="Situação/Ambiente Adequado"
    )
    marcacao = models.CharField(max_length=100, verbose_name="Onde Está Escrito o CA")
    natureza = models.CharField(
        max_length=100, verbose_name="Natureza (Nacional ou Importado)"
    )
    observacao = models.TextField(blank=True, verbose_name="Observação")
    Tamanho = models.CharField(max_length=50)
    nProcesso = models.CharField(max_length=50, null=True)
    nDoLaudo = models.CharField(max_length=50, null=True)
    # fornecedor = models.ForeignKey(Fornecedor, on_delete=models.DO_NOTHING, null=True) //pq da erro ao colocar esste campo?

    def __str__(self):
        return f"CA: {self.ca} | {self.equipamento} | Situação: {self.situacao}  |  Quantidade: {self.quantidade}"


class Estoque(models.Model):
    quantidade = models.PositiveIntegerField(
    default=0, verbose_name="Quantidade em Estoque"
    )
    delimitador = models.CharField(max_length=10, default='UN',
                             choices=(('CM','Centímetro'), ('UN','Unidade'), ('L','Litro'), ('ML','Milimitro'))
                             )
    preco = models.FloatField()
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    dataDeValidade = models.DateField(verbose_name="Data de Validade")
    def __str__(self):
        return self.id

