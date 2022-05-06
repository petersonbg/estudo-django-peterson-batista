from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import CreateView
from .models import CustomerData


def list_client(request):
    client = CustomerData.objects.all()

    return render(request, "client/list_clients.html", {'client': client})


def client_detail(request, slug=None):
    detail = get_list_or_404(CustomerData, slug=slug)
    return render(request, "client/detail.html", {'detail': detail})


class ClientCreateView(CreateView):
    pass
