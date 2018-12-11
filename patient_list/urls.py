from django.urls import path
from . import views

urlpatterns = [
    path('', views.showList, name="patient_list"),
    path('detail/', views.showDetail, name="patient_detail"),
]