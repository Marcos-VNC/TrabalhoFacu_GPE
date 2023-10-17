from django.db import models


class Produto(models.Model):
    equipamento = models.CharField(max_length=255, verbose_name="Nome do Equipamento")
    ca = models.CharField(max_length=20, verbose_name="Número do CA")
    # possuiCA = models.BooleanField(default=True, verbose_name='Possui CA')
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

    def __str__(self):
        return f"CA: {self.ca} | {self.equipamento} | Situação: {self.situacao}  |  Quantidade: {self.quantidade}"
