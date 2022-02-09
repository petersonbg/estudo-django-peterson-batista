from django import forms
from .models import DadosCad


class FormDadosCad(forms.ModelForm):
    class Meta:
        model = DadosCad
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})
        self.fields['telefone'].widget.attrs.update({'class': 'mask-telefone'})

