# hello/urls.py
from django.urls import path
from .views import hello, HelloView

urlpatterns = [
    path('hello', hello, name='hello'),
    path('helloWorld', HelloView.as_view(), name='helloview'),
]
