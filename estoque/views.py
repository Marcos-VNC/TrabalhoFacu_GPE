from django.shortcuts import render
from .models import Produto
from .tables import ProdutoTable
from django_tables2 import RequestConfig
from django_tables2.views import SingleTableView
from django.utils import timezone

class EstoqueView(SingleTableView):
    model = Produto
    table_class = ProdutoTable
    template_name = "estoque/estoque.html"
    paginate_by = 9999  # tem q trocar essa merda aqui depois

    def get_table(self, **kwargs):
        table = super().get_table(**kwargs)
        RequestConfig(self.request, paginate=False).configure(table)
        return table

    def get_queryset(self):
        # filtra os validos e vencidos
        status = self.request.GET.get('status')
        queryset = super().get_queryset()
        if status == 'vencido':
            queryset = queryset.filter(dataDeValidade__lt=timezone.now())
        elif status == 'valido':
            queryset = queryset.filter(dataDeValidade__gte=timezone.now())

        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(equipamento__icontains=query)

        return queryset
