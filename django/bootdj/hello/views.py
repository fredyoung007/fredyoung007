from django.views.generic import TemplateView, ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse 

def hello(request):
    return HttpResponse('Hello, World!')

class HelloView(TemplateView): 
    template_name = 'hello.html'