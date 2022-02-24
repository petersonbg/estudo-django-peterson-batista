from django.urls import path

from .views import AboutPageView, HomepageView

app_name = 'pages'

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomepageView.as_view(), name='home'),
]