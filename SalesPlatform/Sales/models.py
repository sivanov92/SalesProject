from django.db import models

class Users(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    position = models.CharField(max_length=15)
    users = models.Manager()

class Contacts(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    contact_details = models.CharField(max_length=300)
    contact_id = models.ForeignKey(Users,on_delete=models.PROTECT)
    contacts = models.Manager() 
# Create your models here.
