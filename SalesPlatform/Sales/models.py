from django.db import models
USER_POSITION = [
    ('Top','Founder/Co-Founder'),
    ('Manager','Manager'),
    ('Dev','Developer'),
    ('SalesRep','SalesRepresentative')
]
class Users(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    position = models.CharField(max_length=15,choices=USER_POSITION)
    users = models.Manager()

class Contacts(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    contact_details = models.CharField(max_length=300)
    contact_id = models.ForeignKey(Users,on_delete=models.PROTECT)
    contacts = models.Manager() 
# Create your models here.
