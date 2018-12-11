from django.urls import path
from . import views

app_name = 'open_consul'

urlpatterns = [
    path('', views.openConsul, name="open-consul"),
    path('^detail-consul/', views.detailConsul, name="detail-consul"),
]
