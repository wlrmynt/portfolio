from django.http import HttpResponse
from django.template import loader


def portfolio(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def detail(request):
  template = loader.get_template('base.html')
  return HttpResponse(template.render())

def picture(request):
  template = loader.get_template('picture.html')
  return HttpResponse(template.render())

def biography(request):
  template = loader.get_template('biography.html')
  return HttpResponse(template.render())


