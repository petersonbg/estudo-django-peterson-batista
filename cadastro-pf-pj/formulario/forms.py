from django import forms
from .models import DadosPessoa, DadosPessoaFisica, DadosPessoaJuridica


class FormPessoaFisica(forms.ModelForm):
    class Meta:
        model_pf = DadosPessoaFisica
        fields_pf = '__all__'


class FormPessoaJuridica(forms.ModelForm):
    class Meta:
        model_pj = DadosPessoaJuridica
        fields_pj = '__all__'
