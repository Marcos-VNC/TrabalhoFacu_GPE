from django.urls import path
from . import views

urlpatterns = [
    path("", views.EstoqueView.as_view(), name="produto"),
    path(
        "adicionar_produto/",
        views.AdicionarProdutoView.as_view(),
        name="adicionar_produto",
    ),
]
