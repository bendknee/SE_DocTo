from django.shortcuts import render

# Create your views here.
def index(request):
    response = {}
    return render(request,'kelola_jadwal.html',response)
