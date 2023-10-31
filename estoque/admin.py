from django.contrib import admin
from .models import Produto,Fornecedor, Endereco


# Register your models here.
admin.site.register(Produto)
admin.site.register(Fornecedor)
admin.site.register(Endereco)
