from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = "__all__"

        widgets = {
            "equipamento": forms.TextInput(attrs={"class": "form-control"}),
            "dataDeValidade": forms.TextInput(attrs={"class": "form-control"}),
            "ca": forms.TextInput(attrs={"class": "form-control"}),
            "situacao": forms.TextInput(attrs={"class": "form-control"}),
            "quantidade": forms.TextInput(attrs={"class": "form-control"}),
            "aprovadoPara": forms.TextInput(attrs={"class": "form-control"}),
            "marcacao": forms.TextInput(attrs={"class": "form-control"}),
            "natureza": forms.TextInput(attrs={"class": "form-control"}),
            "observacao": forms.TextInput(attrs={"class": "form-control"}),
            "Tamanho": forms.TextInput(attrs={"class": "form-control"}),
            "nProcesso": forms.TextInput(attrs={"class": "form-control"}),
            "nDoLaudo": forms.TextInput(attrs={"class": "form-control"}),
        }
