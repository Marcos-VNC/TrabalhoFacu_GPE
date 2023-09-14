from django.db import models

# class EPI(models.Model):
#     nome = models.CharField(max_length=255)
#     numeroCa = models.CharField(max_length=20)
#     validadeCA = models.DateField()

#     def __str__(self):
#         return self.nome


class Produto(models.Model):
    Equipamento = models.CharField(max_length=255, verbose_name="Nome do Equipamento")
    CA = models.CharField(max_length=20, verbose_name="Número do CA", blank=False, null=False)
    PossuiCA = models.BooleanField(default=True, verbose_name='Possui CA')
    Cor = models.CharField(max_length=100)
    DataDeValidade = models.DateField(verbose_name="Data de Validade")
    Situacao = models.CharField(max_length=100, verbose_name="Situação (Aprovado ou Vencido)")
    Quantidade = models.PositiveIntegerField(default=0, verbose_name="Quantidade em Estoque")
    AprovadoPara = models.CharField(max_length=255, verbose_name="Situação/Ambiente Adequado")
    DescricaoEquipamento = models.TextField(verbose_name="Descrição do Equipamento")
    Marcacao = models.CharField(max_length=100, verbose_name="Onde Está Escrito o CA")
    Natureza = models.CharField(max_length=100, verbose_name="Natureza (Nacional ou Importado)")
    Observacao = models.TextField(blank=True, verbose_name="Observação")
    RazaoSocial = models.CharField(max_length=255, verbose_name="Razão Social da Fabricante/Importadora")
    Referencia = models.CharField(max_length=100, verbose_name="Referência")
    Restricao = models.TextField(verbose_name="Restrição (Onde Não Pode Ser Usado)")
    Tamanho = models.CharField(max_length=50)

    def __str__(self):
        return f'CA: {self.CA} | {self.Equipamento} | Situação: {self.Situacao}'