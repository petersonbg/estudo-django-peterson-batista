from django import forms
from models import CustomerData


class PhysicalPerson(forms.ModelForm):
    class Meta:
        model = CustomerData
        exclude = 'cnpj'


class LegalPerson(forms.ModelForm):
    class Meta:
        model = CustomerData
        exclude = 'cpf'
