from django.urls import path
from .views import cart_datails

app_name = 'cart'

urlpatterns = [
    path('', cart_datails, name='detail')
]