from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())
def services(request):
  template = loader.get_template('services.html')
  return HttpResponse(template.render())
def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())

def pricing(request):
  template = loader.get_template('pricing.html')
  return HttpResponse(template.render())

def service_details(request):
    template = loader.get_template('service_details.html')
    return HttpResponse(template.render())

def get_a_quote(request):
    template = loader.get_template('get_a_quote.html')
    return HttpResponse(template.render())
def connexion(request):
    template = loader.get_template('connexion.html')
    return HttpResponse(template.render())
def connexion(request):
    template = loader.get_template('connexion.html')
    return HttpResponse(template.render())

def inscription(request):
    template = loader.get_template('inscription.html')
    return HttpResponse(template.render())
def envoi(request):
    template = loader.get_template('envoi.html')
    return HttpResponse(template.render())






