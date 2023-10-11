from django.db import models


class Login(models.Model):
    # Your model fields
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email




class Register(models.Model):
    # Your model fields
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    date = models.Aggregate(max_length=20)
    mru_phone_number = models.Aggregate(max_length=20)
    sex = models.Aggregate(max_length=10)
    def __str__(self):
        return self.name

# Create your models here.