from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Submarine(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100,unique=True)
    year=models.IntegerField()
    country=models.CharField(max_length=50)
    operational=models.BooleanField(default=True)


class Driver(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100,unique=True)
    service_years=models.IntegerField(default=0)

    def increment_service_years(self):
        self.service_years+=1
        self.save()