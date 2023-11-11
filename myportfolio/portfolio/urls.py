from django.urls import path
from . import views

urlpatterns = [
    path('portfolio/', views.portfolio, name='portfolio'),
    path('biography/', views.biography, name='biography'),
    path('picture/', views.picture, name='picture'),
    path('detail/', views.detail, name='detail'),
]