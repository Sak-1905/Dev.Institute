from django.db import models

# Create your models here.
from django.db import models
import random
# Create your models here.



class User(models.Model):
    id=models.IntegerField(primary_key=True)
    username=models.CharField(unique=True,max_length=255)
    email=models.CharField(unique=True,max_length=255)
    amount_of_money=models.IntegerField(default=1000)
    points=models.IntegerField(default=0)

class Card(models.Model):
    id=models.CharField(primary_key=True,max_length=255)
    name_character=models.CharField(max_length=255)
    species=models.CharField(max_length=255)
    house=models.CharField(max_length=255)
    image_url=models.CharField(max_length=1024)
    date_of_birth=models.CharField(max_length=255)
    patronus=models.CharField(max_length=255)
    price=models.IntegerField(default=random.randint(200,2000))
    xp_points=models.IntegerField(default=random.randint(1,10))
    current_owner=models.ForeignKey(User,on_delete=models.CASCADE, related_name='currentOwnertoUser',default=None,null=True,blank=True)
    previous_owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='previousOwnerToUser',default=None,null=True,blank=True)