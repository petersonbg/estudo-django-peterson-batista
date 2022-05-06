from django.urls import path
from .views import ClientCreateView
from . import views

app_name = "client"

urlpatterns = [
    path('register/', ClientCreateView.as_view(), name='customer-registration'),
    path('list_cli/', views.list_client, name='list-clients'),
    path('<slug:slug>/', views.client_detail, name='client-detail'),
]