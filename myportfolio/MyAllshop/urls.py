from django.urls import path
from MyAllshop import views

ulrpatterns = [
    path('', views.MyAllshop, name='MyAllshop'),
]