from django.shortcuts import render
from .models import Patient, Consul_Patient
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def showList(request):
    user = request.user
    consultations = Consul_Patient.objects.filter(consultation__dokter__username = user).order_by('-status')
    value = request.GET.get('search')
    print(value)
    if value:
        consultations = consultations.filter(patient__name__icontains = value)
    return render(request, 'patient_list/list.html', {'consultations': consultations})

@login_required
def orderBy(request):
    user = request.user
    if request.method == "POST":
        value = request.POST["sort"]
    consultations = []
    if value == "1":
        consultations = Consul_Patient.objects.filter(consultation__dokter__username = user).order_by('-status')
    elif value == "2":
        consultations = Consul_Patient.objects.filter(consultation__dokter__username = user).order_by('patient__name')
    elif value == "3":
        consultations = Consul_Patient.objects.filter(consultation__dokter__username = user).order_by('consultation__jamMulai')
    return render(request, 'patient_list/list.html', {'consultations': consultations})


@login_required
def showDetail(request, pk):
    patient = Patient.objects.get(pk=pk)
    consultation = Consul_Patient.objects.get(patient__pk=pk)
    return render(request, 'patient_list/detail.html', {'patient':patient, 'consultation':consultation})