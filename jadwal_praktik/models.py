from django.db import models

# Create your models here.
class Hari(models.Model):
    name = models.CharField(max_length=27)
    statusActive = models.BooleanField(default=True)
   
