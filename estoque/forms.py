from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

    possuiCa = forms.BooleanField(required=False, widget=forms.CheckboxInput, label='Possui CA')
    ca = forms.CharField(max_length=20, required=False, label='Número de CA')

    def clean(self):
        cleaned_data = super().clean()
        possui_ca = cleaned_data.get('possuiCa')
        ca = cleaned_data.get('ca')

        if possui_ca and not ca:
            raise forms.ValidationError('É necessário fornecer um número de CA se o produto possui CA.')
