from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormPessoaFisica
from .forms import FormPessoaJuridica
from .models import DadosPessoa


def lista_cadastro(request):
    cliente = DadosPessoa.objects.all().order_by('id')

    return render(request, 'cadastro/lista_cad.html', {'cliente': cliente})


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
        return render(request, 'cadastro/cadastro_pf.html', {'form': form_pf})


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
        return render(request, 'cadastro/cadastro_pf.html', {'form': form_pj})


def editar_cadastro_pj(request, id):
    cad = get_object_or_404(DadosPessoa, pk=id)
    form_pj = FormPessoaJuridica(instance=cad)

    if request.method == 'POST':
        form_pj = FormPessoaJuridica(request.POST, instance=cad)

        if not form_pj.is_valid():
            return render(request, 'cadastro/edit_pj.html', {'form': form_pj})

        else:
            cad.save()
            return redirect('/')

    else:
        return render(request, 'cadastro/edit_pj.html', {'form': form_pj})


def editar_cadastro_pf(request, id):
    cad = get_object_or_404(DadosPessoa, pk=id)
    form_pf = FormPessoaFisica(instance=cad)

    if request.method == 'POST':
        form_pf = FormPessoaFisica(request.POST, instance=cad)

        if not form_pf.is_valid():
            return render(request, 'cadastro/edit_pf.html', {'form': form_pf})

        else:
            cad.save()
            return redirect('/')

    else:
        return render(request, 'cadastro/edit_pf.html', {'form': form_pf})

