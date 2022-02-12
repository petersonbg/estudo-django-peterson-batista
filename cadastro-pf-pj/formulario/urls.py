from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_cadastro, name='lista-cadastro'),
    path('novocadastro_pf/', views.novo_cadastro_pf, name='novo-cadastro-pf'),
    path('novocadastro_pj/', views.novo_cadastro_pj, name='novo-cadastro-pj'),
    path('cadastro/<int:id>/', views.cadastro, name='cadastro'),
    path('editar/<int:id>/', views.editar_cadastro, name='editar-cadastro'),
]
