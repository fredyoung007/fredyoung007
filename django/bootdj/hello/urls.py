# hello/urls.py
from django.urls import path
from .views import HomeView, hello, HelloView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("hello", hello, name="hello"),
    path("helloWorld", HelloView.as_view(), name="helloview"),
]
