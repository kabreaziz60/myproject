from email.message import Message
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Devis(models.Model) :
    Ville_depart =models.CharField(max_length =100)
    Ville_liavraison =models.CharField(max_length =100)
    Poid_total =models.CharField(max_length =100)
    Dimension =models.CharField(max_length =100)
    Nom =models.CharField(max_length =100)
    Email =models.EmailField(max_length =50)
    Telephone =models.CharField(max_length =100)
    Message =models.TextField()

class Users(models.Model) :
    First_Name =models.CharField(max_length =100)
    Last_Name=models.CharField(max_length =100)
    Birthday = models.DateField(auto_now=True)
    Gender =models.BooleanField(default=True)
    Email =models.EmailField(max_length =50)
    Telephone =models.CharField(max_length =100)
    Pays =models.IntegerField()




    

