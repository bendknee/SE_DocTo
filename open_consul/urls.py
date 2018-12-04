from django.urls import path
from . import views

urlpatterns = [
    path('', views.openConsul, name="open_consul"),
    path('detail/', views.detailConsul, name="detail_consul"),
]
