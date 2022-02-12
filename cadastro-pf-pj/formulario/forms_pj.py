from django import forms
from .models import DadosPessoaJuridica


class FormPessoaJuridica(forms.ModelForm):
    class Meta:
        model = DadosPessoaJuridica
        fields = '__all__'