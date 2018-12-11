from django.conf.urls import url
from .views import jadwal_praktik_senin,jadwal_praktik_selasa,jadwal_praktik_rabu,jadwal_praktik_kamis,jadwal_praktik_jumat,jadwal_praktik_sabtu,jadwal_praktik_minggu,freeze1,freeze2,freeze3,freeze4,freeze5,freeze6,freeze7,aktif1,aktif2,aktif3,aktif4,aktif5,aktif6,aktif7,hapus1,hapus2,hapus3,hapus4,hapus5,hapus6,hapus7

import sys
sys.path.append('../')
from open_consul.views import openConsul
from patient_list.views import showList


#url for app
urlpatterns = [
        url(r'^senin', jadwal_praktik_senin , name='jadwal_praktik_1'),
        url(r'^selasa', jadwal_praktik_selasa, name='jadwal_praktik_2'),
        url(r'^rabu', jadwal_praktik_rabu, name='jadwal_praktik_3'),
        url(r'^kamis', jadwal_praktik_kamis, name='jadwal_praktik_4'),
        url(r'^jumat', jadwal_praktik_jumat, name='jadwal_praktik_5'),
        url(r'^sabtu', jadwal_praktik_sabtu, name='jadwal_praktik_6'),
        url(r'^minggu', jadwal_praktik_minggu, name='jadwal_praktik_7'),
        url(r'^freeze-senin', freeze1 , name='freeze1'),
        url(r'^freeze-selasa', freeze2, name='freeze2'),
        url(r'^freeze-rabu', freeze3, name='freeze3'),
        url(r'^freeze-kamis', freeze4, name='freeze4'),
        url(r'^freeze-jumat', freeze5, name='freeze5'),
        url(r'^freeze-sabtu', freeze6, name='freeze6'),
        url(r'^freeze-minggu', freeze7, name='freeze7'),
        url(r'^active-senin',  aktif1 , name='aktif1'),
        url(r'^active-selasa',  aktif2, name='aktif2'),
        url(r'^active-rabu', aktif3, name='aktif3'),
        url(r'^active-kamis',  aktif4, name='aktif4'),
        url(r'^active-jumat',  aktif5, name='aktif5'),
        url(r'^active-sabtu',  aktif6, name='aktif6'),
        url(r'^active-minggu',  aktif7, name='aktif7'),
        url(r'^hapus-senin/(?P<id>.*)/$', hapus1, name='hapus1'),
        url(r'^hapus-selasa/(?P<id>.*)/$', hapus2, name='hapus2'),
        url(r'^hapus-rabu/(?P<id>.*)/$', hapus3, name='hapus3'),
        url(r'^hapus-kamis/(?P<id>.*)/$', hapus4, name='hapus4'),
        url(r'^hapus-jumat/(?P<id>.*)/$', hapus5, name='hapus5'),
        url(r'^hapus-sabtu/(?P<id>.*)/$', hapus6, name='hapus6'),
        url(r'^hapus-minggu/(?P<id>.*)/$', hapus7, name='hapus7'),
