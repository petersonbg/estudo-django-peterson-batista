from django.shortcuts import render
from django.views.generic import TemplateView


class AboutPageView(TemplateView):
    template_name = 'about.html'


class HomepageView(TemplateView):
    template_name = 'home.html'
