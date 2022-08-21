from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse


class HomeView(TemplateView):
    template_name = "index.html"


def hello(request):
    return HttpResponse("Hello, World!")


class HelloView(TemplateView):
    template_name = "hello.html"

class AboutView(TemplateView):
    template_name = "about.html"