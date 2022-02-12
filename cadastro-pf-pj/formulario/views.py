from django.shortcuts import render, redirect, get_object_or_404
from .forms_pf import FormPessoaFisica
from .forms_pj import FormPessoaJuridica
from .models import DadosPessoaFisica, DadosPessoaJuridica


def lista_cadastro(request):
    cli_pf = DadosPessoaFisica.objects.all().order_by('nome')
    cli_pj = DadosPessoaJuridica.objects.all().order_by('nome')

    clientes = {
        'cli_pf': cli_pf,
        'cli_pj': cli_pj
    }

    return render(request, 'cadastros/lista_cad.html', clientes)


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
