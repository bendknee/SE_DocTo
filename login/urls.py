from django.urls import path
from login import views

urlpatterns = [
    path(r'', views.index, name='index')
]