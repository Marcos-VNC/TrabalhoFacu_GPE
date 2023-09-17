import django_tables2 as tables
from .models import Produto

class ProdutoTable(tables.Table):
    class Meta:
        model = Produto
        template_name = "django_tables2/bootstrap4.html"
        fields = ('id', 'ca', 'equipamento', 'dataDeValidade', 'situacao', 'quantidade')
