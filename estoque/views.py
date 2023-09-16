from django.shortcuts import render
from .models import Produto
from .tables import ProdutoTable
from django_tables2 import RequestConfig


def index(request):
    produtos = Produto.objects.all()
    return render(request, 'estoque/estoque.html', {'produtos': produtos})

def estoque_view(request):
    produtos = Produto.objects.all()
    table = ProdutoTable(produtos)
    RequestConfig(request, paginate=False).configure(table)
    return render(request, "estoque/estoque.html", {"table": table})