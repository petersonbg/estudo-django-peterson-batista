from django.contrib import admin
from .models import DadosPessoaFisica, DadosPessoaJuridica

admin.site.register(DadosPessoaFisica)
admin.site.register(DadosPessoaJuridica)

# Register your models here.
