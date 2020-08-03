from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    position = models.CharField(max_length=15)
    users = models.Manager()

class Contacts(models.Model):
    name = models.CharField(max_length=200)
    contact_details = models.CharField(max_length=300)
    contact_id =models.CharField(max_length=15)
    contacts = models.Manager() 
# Create your models here.
