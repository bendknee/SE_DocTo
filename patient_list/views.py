from django.shortcuts import render

# Create your views here.

def showList(request):
    return render(request, 'patient_list/list.html', {})