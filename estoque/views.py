from django.shortcuts import render, redirect
from .models import Produto
from .tables import ProdutoTable
from django_tables2 import RequestConfig
from django_tables2.views import SingleTableView
from django.utils import timezone
from .forms import ProdutoForm
from django.views import View
import requests
from django.http import JsonResponse


class EstoqueView(SingleTableView):
    model = Produto
    table_class = ProdutoTable
    template_name = "estoque/produto.html"
    paginate_by = 9999  # tem q trocar essa merda aqui depois
    print('0')
    def get_table(self, **kwargs):
        print('teste')
        table = super().get_table(**kwargs)
        print('1')
        RequestConfig(self.request, paginate=False).configure(table)
        print('2')
        return table

    def get_queryset(self):
        # filtra os validos e vencidos
        status = self.request.GET.get("status")
        queryset = super().get_queryset()
        if status == "vencido":
            queryset = queryset.filter(dataDeValidade__lt=timezone.now())
        elif status == "valido":
            queryset = queryset.filter(dataDeValidade__gte=timezone.now())

        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(equipamento__icontains=query)

        return queryset


class AdicionarProdutoView(View):
    template = "estoque/adicionar_produto.html"

    def get(self, request):
        form = ProdutoForm()
        return render(request, self.template, {"form": form})

    def post(self, request):
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            mensagem = "Item adicionado ao estoque"
            return render(
                request, self.template, {"form": ProdutoForm(), "mensagem": mensagem}
            )
        return render(request, self.template, {"form": form})
