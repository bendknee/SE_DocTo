from django.urls import path
from . import views

urlpatterns = [
	path('', views.showList, name="patient_list"),
	path('<int:pk>/detail/', views.showDetail, name="patient_detail"),
	path('order/', views.orderBy, name="order_by"),
	path('delete/<int:consultation_pk>/', views.delete, name='delete-consul'),
]