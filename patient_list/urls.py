from django.urls import path
from . import views

urlpatterns = [
    path('', views.showList, name="patient_list"),
]