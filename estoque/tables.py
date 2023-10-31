import django_tables2 as tables
from .models import Produto


class ProdutoTable(tables.Table):
    class Meta:
        model = Produto

        attrs = {"class": "table table-striped table-dark table-bordered mt-2 mx-1"}
        fields = ("id", "ca", "equipamento", "dataDeValidade", "situacao", "quantidade")
