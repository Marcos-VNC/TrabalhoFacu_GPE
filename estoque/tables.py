import django_tables2 as tables
from .models import Produto

class ProdutoTable(tables.Table):
    equipamento = tables.Column(order_by=("equipamento",))
    ca = tables.Column(order_by=("ca",))
    dataDeValidade = tables.Column(order_by=("dataDeValidade",))
    situacao = tables.Column(order_by=("situacao",))

    class Meta:
        model = Produto
        template_name = "django_tables2/bootstrap4.html"
        per_page = 100