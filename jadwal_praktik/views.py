from django.shortcuts import render
import sys
sys.path.append('../')
from open_consul.models import Consul
from .models import Hari
from django.contrib.auth.decorators import login_required


# Create your views here.

def create_models_hari():
    num = Hari.objects.all().count()
    if num != 7:
        hari = ['Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Minggu']
        for item in hari:
            tambah = Hari.objects.create(name=item)
            tambah.save()


@login_required        
def jadwal_praktik_senin(request):
    create_models_hari()
    status = Hari.objects.get(name='Senin')
    if status.statusActive:
        response = {}
        data = Consul.objects.filter(hariPraktik='Senin')
        response['data'] = data
        return render(request,'kelola_jadwal_1.html',response)
    else:
        return render(request,'freeze1.html',response)


@login_required
def jadwal_praktik_selasa(request):
    create_models_hari()
    status = Hari.objects.get(name='Selasa')
    if status.statusActive:
        response = {}
        data = Consul.objects.filter(hariPraktik='Selasa')
        response['data'] = data
        return render(request, 'kelola_jadwal_2.html',response)
    else:
        return render(request, 'freeze2.html',response)
    

@login_required
def jadwal_praktik_rabu(request):
    create_models_hari()
    status = Hari.objects.get(name='Rabu')
    response = {}
    if status.statusActive:
        response = {}
        data = Consul.objects.filter(hariPraktik='Rabu')
        response['data'] = data
        return render(request, 'kelola_jadwal_3.html',response)
    else:
        return render(request, 'freeze3.html',response)


@login_required    
def jadwal_praktik_kamis(request):
    create_models_hari()
    status = Hari.objects.get(name='Kamis')
    if status.statusActive:
        response = {}
        data = Consul.objects.filter(hariPraktik='Kamis')
        response['data'] = data
        return render(request,'kelola_jadwal_4.html',response)
    else:
         return render(request,'freeze4.html',response)


@login_required        
def jadwal_praktik_jumat(request):
    create_models_hari()
    status = Hari.objects.get(name='Jumat')
    response = {}
    if status.statusActive:
        response = {}
        data = Consul.objects.filter(hariPraktik='Jumat')
        response['data'] = data
        return render(request,'kelola_jadwal_5.html', response)
    else:
         return render(request,'freeze5.html',response)


@login_required        
def jadwal_praktik_sabtu(request):
    create_models_hari()
    status = Hari.objects.get(name='Sabtu')
    if status.statusActive:
        response = {}
        data = Consul.objects.filter(hariPraktik='Sabtu')
        response['data'] = data
        return render(request, 'kelola_jadwal_6.html',response)
    else:
         return render(request,'freeze6.html',response)


@login_required       
def jadwal_praktik_minggu(request):
    create_models_hari()
    status = Hari.objects.get(name='Minggu')
    if status.statusActive:
        response = {}
        data = Consul.objects.filter(hariPraktik='Minggu')
        response['data'] = data
        return render(request, 'kelola_jadwal_7.html',response)
    else:
         return render(request,'freeze7.html',response)


@login_required
def freeze1(request):
    value = Hari.objects.get(name='Senin')
    value.statusActive = False
    value.save()
    response = {}
    return render(request,'freeze1.html', response)


@login_required
def freeze2(request):
    value = Hari.objects.get(name='Selasa')
    value.statusActive = False
    value.save()
    response = {}
    return render(request,'freeze2.html', response)


@login_required
def freeze3(request):
    value = Hari.objects.get(name = 'Rabu')
    value.statusActive = False
    value.save()
    response = {}
    return render (request, 'freeze3.html', response)


@login_required    
def freeze4(request):
    value = Hari.objects.get(name = 'Kamis')
    value.statusActive = False
    value.save()
    response = {}
    return render(request, 'freeze4.html', response)


@login_required
def freeze5(request):
    value = Hari.objects.get(name = 'Jumat')
    value.statusActive = False
    value.save()
    response = {}
    return render(request, 'freeze5.html', response)


@login_required    
def freeze6(request):
    value = Hari.objects.get(name = 'Sabtu')
    value.statusActive = False
    value.save()
    response = {}
    return render(request, 'freeze6.html', response)


@login_required
def freeze7(request):
    value = Hari.objects.get(name = 'Minggu')
    value.statusActive = False
    value.save()
    response = {}
    return render(request, 'freeze7.html', response)


@login_required
def aktif1(request):
    value = Hari.objects.get(name = 'Senin')
    value.statusActive = True
    value.save()
    response = {}
    data = Consul.objects.filter(hariPraktik='Senin')
    response['data'] = data
    return render(request, 'kelola_jadwal_1.html',response)


@login_required
def aktif2(request):
    value = Hari.objects.get(name = 'Selasa')
    value.statusActive = True
    value.save()
    response = {}
    data = Consul.objects.filter(hariPraktik='Selasa')
    response['data'] = data
    return render(request, 'kelola_jadwal_2.html',response)


@login_required
def aktif3(request):
    value = Hari.objects.get(name = 'Rabu')
    value.statusActive = True
    value.save()
    response = {}
    data = Consul.objects.filter(hariPraktik='Rabu')
    response['data'] = data
    return render(request, 'kelola_jadwal_3.html',response)


@login_required
def aktif4(request):
    value = Hari.objects.get(name = 'Kamis')
    value.statusActive = True
    value.save()
    response = {}
    data = Consul.objects.filter(hariPraktik='Kamis')
    response['data'] = data
    return render(request, 'kelola_jadwal_4.html',response)


@login_required
def aktif5(request):
    value = Hari.objects.get(name = 'Jumat')
    value.statusActive = True
    value.save()
    response = {}
    data = Consul.objects.filter(hariPraktik='Jumat')
    response['data'] = data
    return render(request, 'kelola_jadwal_5.html',response)


@login_required
def aktif6(request):
    value = Hari.objects.get(name = 'Sabtu')
    value.statusActive = True
    value.save()
    response = {}
    data = Consul.objects.filter(hariPraktik='Sabtu')
    response['data'] = data
    return render(request, 'kelola_jadwal_6.html',response)


@login_required
def aktif7(request):
    value = Hari.objects.get(name = 'Minggu')
    value.statusActive = True
    value.save()
    response = {}
    data = Consul.objects.filter(hariPraktik='Minggu')
    response['data'] = data
    return render(request, 'kelola_jadwal_7.html',response)


@login_required
def hapus1(request,id):
    value = Consul.objects.get(id = id)
    value.delete()
    response = {}
    data = Consul.objects.filter(hariPraktik='Senin')
    response['data'] = data
    return render(request,'kelola_jadwal_1.html',response)


@login_required
def hapus2(request,id):
    value = Consul.objects.get(id = id)
    value.delete()
    response = {}
    data = Consul.objects.filter(hariPraktik='Selasa')
    response['data'] = data
    return render(request,'kelola_jadwal_2.html',response)


@login_required
def hapus3(request,id):
    value = Consul.objects.get(id = id)
    value.delete()
    response = {}
    data = Consul.objects.filter(hariPraktik='Rabu')
    response['data'] = data
    return render(request,'kelola_jadwal_3.html',response)


@login_required	
def hapus4(request,id):
    value = Consul.objects.get(id = id)
    value.delete()
    response = {}
    data = Consul.objects.filter(hariPraktik='Kamis')
    response['data'] = data
    return render(request,'kelola_jadwal_4.html',response)


@login_required	
def hapus5(request,id):
    value = Consul.objects.get(id = id)
    value.delete()
    response = {}
    data = Consul.objects.filter(hariPraktik='Jumat')
    response['data'] = data
    return render(request,'kelola_jadwal_5.html',response)


@login_required	
def hapus6(request,id):
    value = Consul.objects.get(id = id)
    value.delete()
    response = {}
    data = Consul.objects.filter(hariPraktik='Sabtu')
    response['data'] = data
    return render(request,'kelola_jadwal_6.html',response)


@login_required	
def hapus7(request,id):
    value = Consul.objects.get(id = id)
    value.delete()
    response = {}
    data = Consul.objects.filter(hariPraktik='Minggu')
    response['data'] = data
    return render(request,'kelola_jadwal_7.html',response)
