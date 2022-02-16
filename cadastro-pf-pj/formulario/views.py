from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormPessoaFisica
from .forms import FormPessoaJuridica
from .models import DadosPessoa
from django.views import generic


def lista_cadastro(request):
    cliente = DadosPessoa.objects.all().order_by('nome')

    return render(request, 'cadastros/lista_cad.html', {'cliente': cliente})


def novo_cadastro_pf(request):
    if request.method == 'POST':
        form_pf = FormPessoaFisica(request.POST)

        if form_pf.is_valid():
            cad = form_pf.save()
            cad.user = request.user
            cad.save()
            return redirect('/')

    else:
        form_pf = FormPessoaFisica

        return render(request, 'cadastros/cadastro_pf.html', {'form': form_pf})


def novo_cadastro_pj(request):
    if request.method == 'POST':
        form_pj = FormPessoaJuridica(request.POST)

        if form_pj.is_valid():
            cad = form_pj.save()
            cad.user = request.user
            cad.save()
            return redirect('/')

    else:
        form_pj = FormPessoaJuridica

        return render(request, 'cadastros/cadastro_pf.html', {'form': form_pj})


def cadastro(request):
    pass


def editar_cadastro(request):
    pass
