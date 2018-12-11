from django.shortcuts import render
from .models import Consul
from .forms import ConsulForm

# Create your views here.
response = {}


def openConsul(request):
    html = 'open_consul/open-consul.html'
    response['consul_form'] = ConsulForm
    return render(request, html, response)

def detailConsul(request):
    form = ConsulForm(request.POST or None)
    if(request.method == 'POST' and form.is_valid()):
        response['hariPraktik'] = request.POST['hariPraktik']
        response['jamMulai'] = request.POST['jamMulai']
        response['jamSelesai'] = request.POST['jamSelesai']
        response['lokasiPraktik'] = request.POST['lokasiPraktik']
        consul = Consul(hariPraktik=response['hariPraktik'],jamMulai=response['jamMulai'], 
        jamSelesai=response['jamSelesai'], lokasiPraktik=response['lokasiPraktik'])
        consul.save()
        html = 'open_consul/detail-consul.html'
        return render(request, html, response)

