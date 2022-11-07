from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.about, name='about'),
    path('services/', views.services, name='services'), 
    path('contact/', views.contact, name='contact'), 
    path('pricing/', views.pricing, name='pricing'), 
    path('service_details/', views.service_details, name='service_details'), 
    path('get_a_quote/', views.get_a_quote, name='get_a_quote'), 
    path('connexion/', views.connexion, name='connexion'), 
    path('inscription/', views.inscription, name='inscription'), 
    path('envoi/', views.envoi, name='envoi'), 


]