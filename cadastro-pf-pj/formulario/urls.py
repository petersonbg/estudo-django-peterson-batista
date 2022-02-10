from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_cadastro, name='lista-cadastro'),
    path('novocadastro/', views.novo_cadastro, name='novo-cadastro'),
    path('cadastro/<int:id>/', views.cadastro, name='cadastro'),
    path('editar/<int:id>/', views.editar_cadastro, name='editar-cadastro'),
]
