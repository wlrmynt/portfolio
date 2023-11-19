from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Detail, Contact, Member


def portfolio(request):
   
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def detail(request):
  data_detail = Detail.objects.all()  
  template = loader.get_template('base.html')
  context = {
    'salam' : "Halo ini Detail",
    'details' : data_detail,
  }
  return HttpResponse(template.render(context, request))


def picture(request):
  template = loader.get_template('picture.html')
  return HttpResponse(template.render())

def biography(request):
  template = loader.get_template('biography.html')
  return HttpResponse(template.render())


