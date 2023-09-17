from django.shortcuts import render
from .models import Produto
from .tables import ProdutoTable
from django_tables2 import RequestConfig
from django_tables2.views import SingleTableView

def index(request):
    produtos = Produto.objects.all()
    return render(request, 'estoque/estoque.html', {'produtos': produtos})

class EstoqueView(SingleTableView):
    model = Produto
    table_class = ProdutoTable
    template_name = "estoque/estoque.html"
    paginate_by = 9999  # tem q trocar essa merda aqui depois

    def get_table(self, **kwargs):
        table = super().get_table(**kwargs)
        RequestConfig(self.request, paginate=False).configure(table)
        return table
    
