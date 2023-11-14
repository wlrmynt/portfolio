from django.contrib import admin
from django.urls import include, path
from MyAllshop.views import MyAllshop
from portfolio.views import *


urlpatterns = [
 path('portfolio/', portfolio, name='portfolio'),
    path('biography/', biography, name='biography'),
    path('picture/', picture, name='picture'),
    path('detail/', detail, name='detail'),
    path('allshop', MyAllshop, name='MyAllshop'),
    path('admin/', admin.site.urls),
]