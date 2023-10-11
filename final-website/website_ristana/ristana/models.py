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

    def __str__(self):
        return self.name

# Create your models here.