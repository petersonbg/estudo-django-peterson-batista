from django import forms
from .models import DadosPessoa


class FormPessoaFisica(forms.ModelForm):
    class Meta:
        model = DadosPessoa
        exclude = 'cnpj', 'insc_estadual'


class FormPessoaJuridica(forms.ModelForm):
    class Meta:
        model = DadosPessoa
        exclude = 'sexo', 'cpf', 'rg', 'dt_nasc'
