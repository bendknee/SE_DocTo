from django.contrib import admin
from .models import Patient, Consul_Patient
# Register your models here.

admin.site.register(Patient)
admin.site.register(Consul_Patient)