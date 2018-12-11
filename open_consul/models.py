from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Consul(models.Model):
    hariPraktik = models.TextField()
    jamMulai = models.TextField(default='00.00')
    jamSelesai = models.TextField(default='00.00')
    lokasiPraktik = models.TextField()
    dokter = models.ForeignKey(User, on_delete=models.CASCADE,default=1)