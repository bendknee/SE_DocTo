from django.shortcuts import render

# Create your views here.

def openConsul(request):
    return render(request, 'open_consul/open-consul.html', {})

def detailConsul(request):
    return render(request, 'open_consul/detail-consul.html', {})

