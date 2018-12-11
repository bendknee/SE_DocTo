from django.db import models

# Create your models here.
class Consul(models.Model):
    hariPraktik = models.TextField()
    jamMulai = models.TextField(default='00.00')
    jamSelesai = models.TextField(default='00.00')
    lokasiPraktik = models.TextField()