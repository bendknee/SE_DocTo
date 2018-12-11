from django.db import models
from open_consul.models import Consul

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    address =models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Consul_Patient(models.Model):
    consultation = models.ForeignKey(Consul, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    status = models.BooleanField()

    def __str__(self):
        return self.consultation.hariPraktik + " " + self.consultation.dokter.username + " " + self.patient.name

