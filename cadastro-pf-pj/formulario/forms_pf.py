from django import forms
from .models import DadosPessoaFisica


class FormPessoaFisica(forms.ModelForm):
    class Meta:
        model = DadosPessoaFisica
        fields = '__all__'
