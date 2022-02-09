from django.shortcuts import render, redirect
from .models import DadosCad
from .forms import FormDadosCad


def novo_cadastro(request):
    if request.method == 'POST':
        form = FormDadosCad(request.POST)

        if form.is_valid():
            cad = form.save()
            cad.user = request.user
            cad.save()
            return redirect('/')

    else:
        form = FormDadosCad

    return render(request, 'cadastro/formularios.html', {'form': form})
