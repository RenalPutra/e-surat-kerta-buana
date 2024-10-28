from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
import requests
from django.shortcuts import get_object_or_404
from .models import *
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.conf import settings
import os
from django.core.exceptions import SuspiciousFileOperation
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def dashboard(request):
    template_name = "backend/dashboard.html"
    
    total_users = User.objects.count()
    
    # Menghitung total surat dari masing-masing model
    total_surat_permohonan_ktp = SuketPermohonanKTP.objects.count()
    total_surat_belum_menikah = SuketBelumMenikah.objects.count()
    total_surat_tidak_mampu = SuketTidakMampu.objects.count()
    total_skck = SKCK.objects.count()
    total_suket_ktp_beda_nama = SuketKTPBedaNama.objects.count()
    total_suket_ahli_waris = SuketAhliWaris.objects.count()
    total_suket_mtq = SuketMTQ.objects.count()
    total_suket_kehilangan = SuketKehilangan.objects.count()
    total_suket_kelahiran = SuketKelahiran.objects.count()
    total_suket_kematian = SuketKematian.objects.count()
    total_suket_penghasilan_tidak_tetap = SuketPenghasilanTidakTetap.objects.count()
    total_suket_usaha = SuketUsaha.objects.count()
    total_suket_vaksin_nikah = SuketVaksinNikah.objects.count()
    total_suket_pindah_nikah = SuketPindahNikah.objects.count()
    total_suket_rek_kel_tani = SuketRekKelTani.objects.count()
    
    total_aduan = PengaduanAsing.objects.count()
    
    blg = Blog.objects.all().order_by('-id')[:5]
    annc = Pengumuman.objects.all().order_by('-id')[:5]

    # Menjumlahkan semua surat
    total_surat = (
        total_surat_permohonan_ktp +
        total_surat_belum_menikah +
        total_surat_tidak_mampu +
        total_skck +
        total_suket_ktp_beda_nama +
        total_suket_ahli_waris +
        total_suket_mtq +
        total_suket_kehilangan +
        total_suket_kelahiran +
        total_suket_kematian +
        total_suket_penghasilan_tidak_tetap +
        total_suket_usaha +
        total_suket_vaksin_nikah +
        total_suket_pindah_nikah +
        total_suket_rek_kel_tani
    )# Menghitung jumlah seluruh user
    
     # Ambil surat-surat terbaru
    recent_surat = []

     # Gabungkan semua surat dan urutkan berdasarkan tanggal
    surat_permohonan_ktp = SuketPermohonanKTP.objects.all().order_by('-date')
    suket_belum_menikah = SuketBelumMenikah.objects.all().order_by('-date')
    suket_tidak_mampu = SuketTidakMampu.objects.all().order_by('-date')
    skck = SKCK.objects.all().order_by('-date')
    suket_ktp_beda_nama = SuketKTPBedaNama.objects.all().order_by('-date')
    suket_ahli_waris = SuketAhliWaris.objects.all().order_by('-date')
    suket_mtq = SuketMTQ.objects.all().order_by('-date')
    suket_kehilangan = SuketKehilangan.objects.all().order_by('-date')
    suket_kelahiran = SuketKelahiran.objects.all().order_by('-date')
    suket_kematian = SuketKematian.objects.all().order_by('-date')
    suket_penghasilan_tidak_tetap = SuketPenghasilanTidakTetap.objects.all().order_by('-date')
    suket_usaha = SuketUsaha.objects.all().order_by('-date')
    suket_vaksin_nikah = SuketVaksinNikah.objects.all().order_by('-date')
    suket_pindah_nikah = SuketPindahNikah.objects.all().order_by('-date')
    suket_rek_kel_tani = SuketRekKelTani.objects.all().order_by('-date')

    # Masukkan data surat dan tipe surat ke recent_surat
    for surat in surat_permohonan_ktp:
        recent_surat.append({'surat': surat, 'type': 'Surat Permohonan KTP'})
    for surat in suket_belum_menikah:
        recent_surat.append({'surat': surat, 'type': 'Surat Keterangan Belum Menikah'})
    for surat in suket_tidak_mampu:
        recent_surat.append({'surat': surat, 'type': 'Surat Keterangan Tidak Mampu'})
    for surat in skck:
        recent_surat.append({'surat': surat, 'type': 'SKCK'})
    for surat in suket_ktp_beda_nama:
        recent_surat.append({'surat': surat, 'type': 'Surat Keterangan KTP Beda Nama'})
    for surat in suket_ahli_waris:
        recent_surat.append({'surat': surat, 'type': 'Surat Keterangan Ahli Waris'})
    for surat in suket_mtq:
        recent_surat.append({'surat': surat, 'type': 'Surat Keterangan MTQ'})
    for surat in suket_kehilangan:
        recent_surat.append({'surat': surat, 'type': 'Surat Keterangan Kehilangan'})
    for surat in suket_kelahiran:
        recent_surat.append({'surat': surat, 'type': 'Surat Keterangan Kelahiran'})
    for surat in suket_kematian:
        recent_surat.append({'surat': surat, 'type': 'Surat Keterangan Kematian'})
    for surat in suket_penghasilan_tidak_tetap:
        recent_surat.append({'surat': surat, 'type': 'Surat Keterangan Penghasilan Tidak Tetap'})
    for surat in suket_usaha:
        recent_surat.append({'surat': surat, 'type': 'Surat Keterangan Usaha'})
    for surat in suket_vaksin_nikah:
        recent_surat.append({'surat': surat, 'type': 'Surat Keterangan Vaksin Nikah'})
    for surat in suket_pindah_nikah:
        recent_surat.append({'surat': surat, 'type': 'Surat Keterangan Pindah Nikah'})
    for surat in suket_rek_kel_tani:
        recent_surat.append({'surat': surat, 'type': 'Surat Rek Kel Tani'})
    
    # Urutkan recent_surat berdasarkan tanggal surat
    recent_surat = sorted(recent_surat, key=lambda x: x['surat'].date, reverse=True)
    
    context = {
        'total_users': total_users, 
        'total_surat' : total_surat,
        'total_aduan' :total_aduan,
        'recent_surat': recent_surat,
        'blg': blg,
        'annc':annc,
        'title': 'Dashboard',
    }
    
    return render(request, template_name, context)


@login_required
def suketpermohonanktp(request):
    template_name = "backend/suketpermohonanktp.html"
    
    suket = SuketPermohonanKTP.objects.all().order_by('-date')
    private = SuketPermohonanKTP.objects.filter(penulis=request.user).order_by('-date')
    
    if request.method == "POST":
        fs = FileSystemStorage()

        # Menyimpan file-file yang di-upload
        pengantar_rt_file = request.FILES.get("pengantar_rt")
        if pengantar_rt_file:
            # Mengubah nama file dengan menghapus spasi
            pengantar_rt_file.name = pengantar_rt_file.name.replace(' ', '_')
            pengantar_rt_filename = fs.save(pengantar_rt_file.name, pengantar_rt_file)
            pengantar_rt_url = fs.url(pengantar_rt_filename)
        else:
            pengantar_rt_url = None
        
        scankk_file = request.FILES.get("scankk")
        if scankk_file:
            # Mengubah nama file dengan menghapus spasi
            scankk_file.name = scankk_file.name.replace(' ', '_')
            scankk_filename = fs.save(scankk_file.name, scankk_file)
            scankk_url = fs.url(scankk_filename)
        else:
            scankk_url = None

        scan_ijazah_akta_file = request.FILES.get("scanijasahakta")
        if scan_ijazah_akta_file:
            # Mengubah nama file dengan menghapus spasi
            scan_ijazah_akta_file.name = scan_ijazah_akta_file.name.replace(' ', '_')
            scan_ijazah_akta_filename = fs.save(scan_ijazah_akta_file.name, scan_ijazah_akta_file)
            scan_ijazah_akta_url = fs.url(scan_ijazah_akta_filename)
        else:
            scan_ijazah_akta_url = None

        # Menyimpan data SuketPermohonanKTP
        SuketPermohonanKTP.objects.create(
            penulis=request.user,
            nama=request.POST.get("inputNama"),
            nokk=request.POST.get("inputNOKK"),
            nik=request.POST.get("inputNIK"),
            alamat=request.POST.get("inputAlamat"),
            pengantarrt=pengantar_rt_url,
            scankk=scankk_url,
            scanijasahakta=scan_ijazah_akta_url,
        )
    
        return redirect('suketpermohonanktp')
    
    context = {
        "suket": suket,
        'private': private,
        'title': 'Permohonan KTP'
    }
    
    return render(request, template_name, context)

@login_required
def edit_suketpermohonanktp(request, id):
    template_name = "backend/suketpermohonanktp.html"
    
    suket_id = get_object_or_404(SuketPermohonanKTP, id=id)
    
    if request.method == "POST":
        fs = FileSystemStorage()

        # Mengecek file baru yang di-upload dan menyimpannya
        pengantar_rt_file = request.FILES.get("pengantar_rt")
        if pengantar_rt_file:
            pengantar_rt_file.name = pengantar_rt_file.name.replace(' ', '_')
            pengantar_rt_filename = fs.save(pengantar_rt_file.name, pengantar_rt_file)
            suket_id.pengantarrt = fs.url(pengantar_rt_filename)
        
        scankk_file = request.FILES.get("scankk")
        if scankk_file:
            scankk_file.name = scankk_file.name.replace(' ', '_')
            scankk_filename = fs.save(scankk_file.name, scankk_file)
            suket_id.scankk = fs.url(scankk_filename)
        
        scan_ijazah_akta_file = request.FILES.get("scanijasahakta")
        if scan_ijazah_akta_file:
            scan_ijazah_akta_file.name = scan_ijazah_akta_file.name.replace(' ', '_')
            scan_ijazah_akta_filename = fs.save(scan_ijazah_akta_file.name, scan_ijazah_akta_file)
            suket_id.scanijasahakta = fs.url(scan_ijazah_akta_filename)

        # Mengedit data SuketPermohonanKTP
        suket_id.penulis = request.user
        suket_id.nama = request.POST.get("inputNama")
        suket_id.nokk = request.POST.get("inputNOKK")
        suket_id.nik = request.POST.get("inputNIK")
        suket_id.alamat = request.POST.get("inputAlamat")
        suket_id.date = timezone.now()
        suket_id.status = 'review'
        
        suket_id.save()
        
        return redirect('suketpermohonanktp')
    
    context = {
        "value": suket_id
    }
    
    return render(request, template_name, context)

@login_required
def setujui_suketpermohonanktp(request, id):
    if request.user.is_superuser:
        suket = get_object_or_404(SuketPermohonanKTP, id=id)
        suket.status = 'approved'  # Mengubah status menjadi Disetujui
        suket.save()
    return redirect('suketpermohonanktp')

@login_required
def tolak_suketpermohonanktp(request, id):
    if request.user.is_superuser:
        suket = get_object_or_404(SuketPermohonanKTP, id=id)
        suket.status = 'rejected'  # Mengubah status menjadi Ditolak
        suket.save()
    return redirect('suketpermohonanktp')

@login_required
def delete_suketpermohonanktp(request, id):
    SuketPermohonanKTP.objects.get(id=id).delete()
    return redirect('suketpermohonanktp')

@login_required
def print_suketpermohonanktp(request, id):
    template_name = "surat/surat-permohonan-ktp.html"
    surat = get_object_or_404(SuketPermohonanKTP, id=id)

    context = {
        'nama': surat.nama,
        'nokk': surat.nokk,
        'nik': surat.nik,
        'alamat': surat.alamat,
        'date': surat.date,
    }
    
    return render(request, template_name, context)

@login_required
def detail_suketpermohonanktp(request, id):
    template_name = "backend/detail_suketpermohonanktp.html"
    suket = get_object_or_404(SuketPermohonanKTP, id=id)
    
    context = {
        'suket': suket,
    }
    
    return render(request, template_name, context)

@login_required
def suketbelummenikah(request):
    template_name = "backend/suketbelummenikah.html"
    
    suket = SuketBelumMenikah.objects.all()
    private = SuketBelumMenikah.objects.filter(penulis=request.user)
    
    if request.method == "POST":
       
        SuketBelumMenikah.objects.create(
            penulis=request.user,
            nama=request.POST.get("inputNama"),
            jenis_kelamin=request.POST.get("inputjk"),
            ttl=request.POST.get("inputTtl"),
            suku=request.POST.get("inputSuku"),
            agama=request.POST.get("inputAgama"),
            nik=request.POST.get("inputNIK"),
            alamat=request.POST.get("inputAlamat"),
            persyaratan=request.POST.get("inputPersyaratan"),
            
        )
    
        return redirect('suketbelummenikah')
    
    context={
        "suket":suket,
        'private': private,
    }
    
    return render(request, template_name, context)

@login_required
def edit_suketbelummenikah(request,id):
    template_name = "backend/suketbelummenikah.html"
    
    suket_id = SuketBelumMenikah.objects.get(id=id)
    
    if request.method == "POST":
        penulis=request.user
        nama=request.POST.get("inputNama")
        jenis_kelamin=request.POST.get("inputjk")
        ttl=request.POST.get("inputTtl")
        suku=request.POST.get("inputSuku")
        agama=request.POST.get("inputAgama")
        nik=request.POST.get("inputNIK")
        alamat=request.POST.get("inputAlamat")
        persyaratan=request.POST.get("inputPersyaratan")
        
        suket_id.penulis=penulis
        suket_id.nama=nama
        suket_id.jenis_kelamin=jenis_kelamin
        suket_id.ttl=ttl
        suket_id.suku=suku
        suket_id.agama=agama
        suket_id.nik=nik
        suket_id.alamat=alamat
        suket_id.persyaratan=persyaratan
        suket_id.date=timezone.now()
        suket_id.status='review'
        
        suket_id.save()
        
        return redirect('suketbelummenikah')
    
    context = {
        "value" : suket_id
    }
    
    
    return render(request, template_name, context)

@login_required
def setujui_suketbelummenikah(request, id):
    if request.user.is_superuser:
        suket = get_object_or_404(SuketBelumMenikah, id=id)
        suket.status = 'approved'  # Mengubah status menjadi Disetujui
        suket.save()
    return redirect('suketbelummenikah')   # Redirect ke halaman list

@login_required
def tolak_suketbelummenikah(request, id):
    if request.user.is_superuser:
        suket = get_object_or_404(SuketBelumMenikah, id=id)
        suket.status = 'rejected'  # Mengubah status menjadi Ditolak
        suket.save()
    return redirect('suketbelummenikah')  # Redirect ke halaman list

@login_required
def delete_suketbelummenikah(request,id):
    SuketBelumMenikah.objects.get(id=id).delete()
    
    return redirect('suketbelummenikah')

@login_required
def print_suketbelummenikah(request, id):
    # Mengambil data surat
    
    template_name= "surat/surat-ket-belum-nikah.html"
    surat = get_object_or_404(SuketBelumMenikah, id=id)

    # Mengisi template dengan data surat
    context = {
        'nama': surat.nama,
        'jenis_kelamin': surat.jenis_kelamin,
        'ttl': surat.ttl,
        'suku': surat.suku,
        'agama': surat.agama,
        'nik': surat.nik,
        'alamat': surat.alamat,
        'persyaratan': surat.persyaratan,
        'date': surat.date,
    }
    
    return render(request,template_name, context)

@login_required
def detail_suketbelummenikah(request, id):
    template_name = "backend/detail_suketbelummenikah.html"  # Template baru untuk halaman detail
    
    # Mengambil objek surat berdasarkan ID
    suket = get_object_or_404(SuketBelumMenikah, id=id)
    
    # Mengirim data ke template
    context = {
        'suket': suket,
    }
    
    return render(request, template_name, context)

   
@login_required
def sukettidakmampu(request):
    template_name = "backend/sukettidakmampu.html"
    
    suket = SuketTidakMampu.objects.all()
    private = SuketTidakMampu.objects.filter(penulis=request.user)
    
    if request.method == "POST":
        fs = FileSystemStorage()

        # Menyimpan file-file yang di-upload
        pengantar_rt_file = request.FILES.get("pengantar_rt")
        if pengantar_rt_file:
            # Mengubah nama file dengan mengganti spasi menjadi underscore
            pengantar_rt_file.name = pengantar_rt_file.name.replace(' ', '_')
            pengantar_rt_filename = fs.save(pengantar_rt_file.name, pengantar_rt_file)
            pengantar_rt_url = fs.url(pengantar_rt_filename)
        else:
            pengantar_rt_url = None
        
        scankk_file = request.FILES.get("scankk")
        if scankk_file:
            # Mengubah nama file dengan mengganti spasi menjadi underscore
            scankk_file.name = scankk_file.name.replace(' ', '_')
            scankk_filename = fs.save(scankk_file.name, scankk_file)
            scankk_url = fs.url(scankk_filename)
        else:
            scankk_url = None
       
        # Menyimpan data SuketTidakMampu
        SuketTidakMampu.objects.create(
            penulis=request.user,
            nama=request.POST.get("inputNama"),
            jenis_kelamin=request.POST.get("inputjk"),
            ttl=request.POST.get("inputTtl"),
            suku=request.POST.get("inputSuku"),
            agama=request.POST.get("inputAgama"),
            nik=request.POST.get("inputNIK"),
            alamat=request.POST.get("inputAlamat"),
            pekerjaan=request.POST.get("inputPekerjaan"),
            dusun=request.POST.get("inputDusun"),
            keperluan=request.POST.get("inputKeperluan"),
            pengantarrt=pengantar_rt_url,
            scankk=scankk_url,
        )
    
        return redirect('sukettidakmampu')
    
    context = {
        "suket": suket,
        'private': private
    }
    
    return render(request, template_name, context)

@login_required
def edit_sukettidakmampu(request,id):
    template_name = "backend/sukettidakmampu.html"
    
    suket_id = SuketTidakMampu.objects.get(id=id)
    
    if request.method == "POST":
        
        fs = FileSystemStorage()

        # Mengecek file baru yang di-upload dan menyimpannya
        pengantar_rt_file = request.FILES.get("pengantar_rt")
        
        if pengantar_rt_file:
            pengantar_rt_file.name = pengantar_rt_file.name.replace(' ', '_')
            pengantar_rt_filename = fs.save(pengantar_rt_file.name, pengantar_rt_file)
            suket_id.pengantarrt = fs.url(pengantar_rt_filename)
        
        scankk_file = request.FILES.get("scankk")
       
        if scankk_file:
            scankk_file.name = scankk_file.name.replace(' ', '_')
            scankk_filename = fs.save(scankk_file.name, scankk_file)
            suket_id.scankk = fs.url(scankk_filename)
        
        penulis=request.user
        nama=request.POST.get("inputNama")
        jenis_kelamin=request.POST.get("inputjk")
        ttl=request.POST.get("inputTtl")
        suku=request.POST.get("inputSuku")
        agama=request.POST.get("inputAgama")
        nik=request.POST.get("inputNIK")
        alamat=request.POST.get("inputAlamat")
        pekerjaan= request.POST.get("inputPekerjaan")
        dusun= request.POST.get("inputDusun")
        keperluan = request.POST.get("inputKeperluan")
        
        
        suket_id.penulis=penulis
        suket_id.nama=nama
        suket_id.jenis_kelamin=jenis_kelamin
        suket_id.ttl=ttl
        suket_id.suku=suku
        suket_id.agama=agama
        suket_id.nik=nik
        suket_id.alamat=alamat
        suket_id.date=timezone.now()
        suket_id.pekerjaan= pekerjaan
        suket_id.dusun = dusun
        suket_id.keperluan= keperluan
        suket_id.status='review'
        
        suket_id.save()
        
        return redirect('sukettidakmampu')
    
    context = {
        "value" : suket_id
    }
    
    
    return render(request, template_name, context)

@login_required
def setujui_sukettidakmampu(request, id):
    if request.user.is_superuser:
        suket = get_object_or_404(SuketTidakMampu, id=id)
        suket.status = 'approved'  # Mengubah status menjadi Disetujui
        suket.save()
    return redirect('sukettidakmampu')  # Redirect ke halaman list Suket Tidak Mampu

@login_required
def tolak_sukettidakmampu(request, id):
    if request.user.is_superuser:
        suket = get_object_or_404(SuketTidakMampu, id=id)
        suket.status = 'rejected'  # Mengubah status menjadi Ditolak
        suket.save()
    return redirect('sukettidakmampu')  # Redirect ke halaman list Suket Tidak Mampu

@login_required
def delete_sukettidakmampu(request,id):
    SuketTidakMampu.objects.get(id=id).delete()
    
    return redirect('sukettidakmampu')

@login_required
def print_sukettidakmampu(request, id):
    # Mengambil data surat
    
    template_name= "surat/surat-tidak-mampu.html"
    surat = get_object_or_404(SuketTidakMampu, id=id)

    # Mengisi template dengan data surat
    context = {
        'nama': surat.nama,
        'ttl': surat.ttl,
        'suku': surat.suku,
        'agama': surat.agama,
        'jenis_kelamin': surat.jenis_kelamin,
        'nik': surat.nik,
        'pekerjaan': surat.pekerjaan,
        'dusun': surat.dusun,
        'keperluan': surat.keperluan,
        'alamat': surat.alamat,
        'date': surat.date,
    }
    
    return render(request,template_name, context)

@login_required
def detail_sukettidakmampu(request, id):
    template_name = "backend/detail_sukettidakmampu.html"  # Template baru untuk halaman detail
    
    # Mengambil objek surat berdasarkan ID
    suket = get_object_or_404(SuketTidakMampu, id=id)
    
    # Mengirim data ke template
    context = {
        'suket': suket,
    }
    
    return render(request, template_name, context)

@login_required
def skck(request):
    template_name = "backend/skck.html"
    
    suket = SKCK.objects.all()
    private = SKCK.objects.filter(penulis=request.user)
    
    if request.method == "POST":
        myfile = request.FILES.get("gambar")
        fs = FileSystemStorage()
        
        if myfile:
            # Mengganti spasi pada nama file dengan underscore
            myfile.name = myfile.name.replace(' ', '_')
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)
            gambar = url
        else:
            gambar = None
        
        # Menyimpan data SKCK
        SKCK.objects.create(
            penulis=request.user,
            nama=request.POST.get("inputNama"),
            jenis_kelamin=request.POST.get("inputjk"),
            ttl=request.POST.get("inputTtl"),
            suku=request.POST.get("inputSuku"),
            agama=request.POST.get("inputAgama"),
            nik=request.POST.get("inputNIK"),
            alamat=request.POST.get("inputAlamat"),
            pekerjaan=request.POST.get("inputPekerjaan"),
            kawin=request.POST.get("inputKawin"),
            pendidikanterakhir=request.POST.get("inputPendidikanterakhir"),
            persyaratan=request.POST.get("inputPersyaratan"),
            scanktp=gambar,
        )
    
        return redirect('skck')
    
    context = {
        "suket": suket,
        'private': private
    }
    
    return render(request, template_name, context)

@login_required
def edit_skck(request,id):
    template_name = "backend/skck.html"
    
    suket_id = SKCK.objects.get(id=id)
    
    if request.method == "POST":
        penulis=request.user
        nama=request.POST.get("inputNama")
        jenis_kelamin=request.POST.get("inputjk")
        ttl=request.POST.get("inputTtl")
        suku=request.POST.get("inputSuku")
        agama=request.POST.get("inputAgama")
        nik=request.POST.get("inputNIK")
        alamat=request.POST.get("inputAlamat")
        pekerjaan= request.POST.get("inputPekerjaan")
        kawin = request.POST.get("inputKawin")
        pendidikanterakhir = request.POST.get("inputPendidikanterakhir")
        persyaratan = request.POST.get("inputPersyaratan")
        # Mengecek apakah ada file baru yang di-upload
        myfile = request.FILES.get("gambar")
        
        if myfile:
            # Jika ada file baru yang di-upload, simpan file baru
            fs = FileSystemStorage()
            myfile.name = myfile.name.replace(' ', '_')
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)
            suket_id.scanktp = url  # Mengupdate hanya jika ada file baru
        
        suket_id.penulis=penulis
        suket_id.nama=nama
        suket_id.jenis_kelamin=jenis_kelamin
        suket_id.ttl=ttl
        suket_id.suku=suku
        suket_id.agama=agama
        suket_id.nik=nik
        suket_id.alamat=alamat
        suket_id.date=timezone.now()
        suket_id.pekerjaan= pekerjaan
        suket_id.kawin= kawin
        suket_id.pendidikanterakhir= pendidikanterakhir
        suket_id.persyaratan = persyaratan
        suket_id.status='review'
       
        
        suket_id.save()
        
        return redirect('skck')
    
    context = {
        "value" : suket_id
    }
    
    
    return render(request, template_name, context)

@login_required
def setujui_skck(request, id):
    if request.user.is_superuser:
        skck = get_object_or_404(SKCK, id=id)
        skck.status = 'approved'  # Mengubah status menjadi Disetujui
        skck.save()
    return redirect('skck')  # Redirect ke halaman list SKCK

@login_required
def tolak_skck(request, id):
    if request.user.is_superuser:
        skck = get_object_or_404(SKCK, id=id)
        skck.status = 'rejected'  # Mengubah status menjadi Ditolak
        skck.save()
    return redirect('skck')  # Redirect ke halaman list SKCK

@login_required
def delete_skck(request,id):
    SKCK.objects.get(id=id).delete()
    
    return redirect('skck')

@login_required
def print_skck(request, id):
    # Mengambil data surat
    
    template_name= "surat/skck.html"
    surat = get_object_or_404(SKCK, id=id)

    # Mengisi template dengan data surat
    context = {
        'nama': surat.nama,
        'jenis_kelamin': surat.jenis_kelamin,
        'ttl': surat.ttl,
        'agama': surat.agama,
        'kawin': surat.kawin,
        'pekerjaan': surat.pekerjaan,
        'suku': surat.suku,
        'nik': surat.nik,
        'alamat': surat.alamat,
        'pendidikanterakhir': surat.pendidikanterakhir,
        'persyaratan': surat.persyaratan,
        'date': surat.date,
    }
    
    return render(request,template_name, context)

@login_required
def detail_skck(request, id):
    template_name = "backend/detail_skck.html"  # Template baru untuk halaman detail SKCK
    
    # Mengambil objek SKCK berdasarkan ID
    skck = get_object_or_404(SKCK, id=id)
    
    # Mengirim data ke template
    context = {
        'skck': skck,
    }
    
    return render(request, template_name, context)

@login_required
def suketktpbedanama(request):
    template_name = "backend/suketktpbedanama.html"
    
    suket = SuketKTPBedaNama.objects.all()
    private = SuketKTPBedaNama.objects.filter(penulis=request.user)
    
    if request.method == "POST":
        fs = FileSystemStorage()

        # Menyimpan file-file yang di-upload
        berkas1_file = request.FILES.get("inputBerkas1")
        if berkas1_file:
            # Mengubah nama file dengan mengganti spasi menjadi underscore
            berkas1_file.name = berkas1_file.name.replace(' ', '_')
            berkas1_filename = fs.save(berkas1_file.name, berkas1_file)
            berkas1_url = fs.url(berkas1_filename)
        else:
            berkas1_url = None
        
        berkas2_file = request.FILES.get("inputBerkas2")
        if berkas2_file:
            # Mengubah nama file dengan mengganti spasi menjadi underscore
            berkas2_file.name = berkas2_file.name.replace(' ', '_')
            berkas2_filename = fs.save(berkas2_file.name, berkas2_file)
            berkas2_url = fs.url(berkas2_filename)
        else:
            berkas2_url = None
        
        # Menyimpan data SuketKTPBedaNama
        SuketKTPBedaNama.objects.create(
            penulis=request.user,
            nama=request.POST.get("inputNama"),
            jenis_kelamin=request.POST.get("inputjk"),
            ttl=request.POST.get("inputTtl"),
            agama=request.POST.get("inputAgama"),
            alamat=request.POST.get("inputAlamat"),
            pekerjaan=request.POST.get("inputPekerjaan"),
            namadokumen1=request.POST.get("inputNamaDokumen1"),
            dokumen1=request.POST.get("inputDokumen1"),
            namadokumen2=request.POST.get("inputNamaDokumen2"),
            dokumen2=request.POST.get("inputDokumen2"),
            berkas1=berkas1_url,
            berkas2=berkas2_url,
        )
    
        return redirect('suketktpbedanama')
    
    context = {
        "suket": suket,
        'private': private,
    }
    
    return render(request, template_name, context)

@login_required
def edit_suketktpbedanama(request, id):
    template_name = "backend/suketktpbedanama.html"
    
    suket_id = SuketKTPBedaNama.objects.get(id=id)
    
    if request.method == "POST":
        fs = FileSystemStorage()

        # Mengecek file baru yang di-upload dan menyimpannya
        berkas1_file = request.FILES.get("inputBerkas1")
        if berkas1_file:
            # Mengubah nama file dengan mengganti spasi menjadi underscore
            berkas1_file.name = berkas1_file.name.replace(' ', '_')
            berkas1_filename = fs.save(berkas1_file.name, berkas1_file)
            suket_id.berkas1 = fs.url(berkas1_filename)
        
        berkas2_file = request.FILES.get("inputBerkas2")
        if berkas2_file:
            # Mengubah nama file dengan mengganti spasi menjadi underscore
            berkas2_file.name = berkas2_file.name.replace(' ', '_')
            berkas2_filename = fs.save(berkas2_file.name, berkas2_file)
            suket_id.berkas2 = fs.url(berkas2_filename)
        
        # Mengedit data SuketKTPBedaNama
        suket_id.penulis = request.user
        suket_id.nama = request.POST.get("inputNama")
        suket_id.jenis_kelamin = request.POST.get("inputjk")
        suket_id.ttl = request.POST.get("inputTtl")
        suket_id.agama = request.POST.get("inputAgama")
        suket_id.alamat = request.POST.get("inputAlamat")
        suket_id.pekerjaan = request.POST.get("inputPekerjaan")
        suket_id.namadokumen1 = request.POST.get("inputNamaDokumen1")
        suket_id.dokumen1 = request.POST.get("inputDokumen1")
        suket_id.namadokumen2 = request.POST.get("inputNamaDokumen2")
        suket_id.dokumen2 = request.POST.get("inputDokumen2")
        suket_id.date = timezone.now() 
        suket_id.status = 'review'
        
        suket_id.save()
        
        return redirect('suketktpbedanama')
    
    context = {
        "value": suket_id
    }
    
    return render(request, template_name, context)

@login_required
def setujui_suketktpbedanama(request, id):
    if request.user.is_superuser:
        suket = get_object_or_404(SuketKTPBedaNama, id=id)
        suket.status = 'approved'  # Mengubah status menjadi Disetujui
        suket.save()
    return redirect('suketktpbedanama')  # Redirect ke halaman list Suket KTP Beda Nama

@login_required
def tolak_suketktpbedanama(request, id):
    if request.user.is_superuser:
        suket = get_object_or_404(SuketKTPBedaNama, id=id)
        suket.status = 'rejected'  # Mengubah status menjadi Ditolak
        suket.save()
    return redirect('suketktpbedanama')  # Redirect ke halaman list Suket KTP Beda Nama

@login_required
def delete_suketktpbedanama(request, id):
 
    SuketKTPBedaNama.objects.get(id=id).delete()
    
    return redirect('suketktpbedanama')

@login_required
def print_suketktpbedanama(request, id):
    # Mengambil data surat
    
    template_name= "surat/surat-ket-beda-nama-dgn-ktp.html"
    surat = get_object_or_404(SuketKTPBedaNama, id=id)

    # Mengisi template dengan data surat
    context = {
        'nama': surat.nama,
        'ttl': surat.ttl,
        'jenis_kelamin': surat.jenis_kelamin,
        'pekerjaan': surat.pekerjaan,
        'agama': surat.agama,
        'alamat': surat.alamat,
        'namadokumen1': surat.namadokumen1,
        'dokumen1': surat.dokumen1,
        'namadokumen2': surat.namadokumen2,
        'dokumen2': surat.dokumen2,
        'date': surat.date,
    }
    
    return render(request,template_name, context)

@login_required
def detail_suketktpbedanama(request, id):
    template_name = "backend/detail_suketktpbedanama.html"  # Template untuk halaman detail
    
    # Mengambil objek SuketKTPBedaNama berdasarkan ID
    suket = get_object_or_404(SuketKTPBedaNama, id=id)
    
    # Mengirim data ke template
    context = {
        'suket': suket,
    }
    
    return render(request, template_name, context)

@login_required
def suketahliwaris(request):
    template_name = "backend/suketahliwaris.html"
    
    suket = SuketAhliWaris.objects.all()
    private = SuketAhliWaris.objects.filter(penulis=request.user)
    
    if request.method == "POST":
        # Menyimpan file-file yang di-upload
        fs = FileSystemStorage()

        skkematian_file = request.FILES.get("skkematian")
        if skkematian_file:
            skkematian_filename = skkematian_file.name.replace(" ", "_")
            skkematian_filename = fs.save(skkematian_filename, skkematian_file)
            skkematian_url = fs.url(skkematian_filename)
        else:
            skkematian_url = None

        scanktpkkahliwaris1_file = request.FILES.get("scanktpkkahliwaris1")
        if scanktpkkahliwaris1_file:
            scanktpkkahliwaris1_filename = scanktpkkahliwaris1_file.name.replace(" ", "_")
            scanktpkkahliwaris1_filename = fs.save(scanktpkkahliwaris1_filename, scanktpkkahliwaris1_file)
            scanktpkkahliwaris1_url = fs.url(scanktpkkahliwaris1_filename)
        else:
            scanktpkkahliwaris1_url = None

        scanktpkkahliwaris2_file = request.FILES.get("scanktpkkahliwaris2")
        if scanktpkkahliwaris2_file:
            scanktpkkahliwaris2_filename = scanktpkkahliwaris2_file.name.replace(" ", "_")
            scanktpkkahliwaris2_filename = fs.save(scanktpkkahliwaris2_filename, scanktpkkahliwaris2_file)
            scanktpkkahliwaris2_url = fs.url(scanktpkkahliwaris2_filename)
        else:
            scanktpkkahliwaris2_url = None

        scanktpkkahliwaris3_file = request.FILES.get("scanktpkkahliwaris3")
        if scanktpkkahliwaris3_file:
            scanktpkkahliwaris3_filename = scanktpkkahliwaris3_file.name.replace(" ", "_")
            scanktpkkahliwaris3_filename = fs.save(scanktpkkahliwaris3_filename, scanktpkkahliwaris3_file)
            scanktpkkahliwaris3_url = fs.url(scanktpkkahliwaris3_filename)
        else:
            scanktpkkahliwaris3_url = None

        scanktpkkahliwaris4_file = request.FILES.get("scanktpkkahliwaris4")
        if scanktpkkahliwaris4_file:
            scanktpkkahliwaris4_filename = scanktpkkahliwaris4_file.name.replace(" ", "_")
            scanktpkkahliwaris4_filename = fs.save(scanktpkkahliwaris4_filename, scanktpkkahliwaris4_file)
            scanktpkkahliwaris4_url = fs.url(scanktpkkahliwaris4_filename)
        else:
            scanktpkkahliwaris4_url = None

        scanktpsaksi1_file = request.FILES.get("scanktpsaksi1")
        if scanktpsaksi1_file:
            scanktpsaksi1_filename = scanktpsaksi1_file.name.replace(" ", "_")
            scanktpsaksi1_filename = fs.save(scanktpsaksi1_filename, scanktpsaksi1_file)
            scanktpsaksi1_url = fs.url(scanktpsaksi1_filename)
        else:
            scanktpsaksi1_url = None

        scanktpsaksi2_file = request.FILES.get("scanktpsaksi2")
        if scanktpsaksi2_file:
            scanktpsaksi2_filename = scanktpsaksi2_file.name.replace(" ", "_")
            scanktpsaksi2_filename = fs.save(scanktpsaksi2_filename, scanktpsaksi2_file)
            scanktpsaksi2_url = fs.url(scanktpsaksi2_filename)
        else:
            scanktpsaksi2_url = None

        # Menyimpan data SuketAhliWaris
        SuketAhliWaris.objects.create(
            penulis=request.user,
            almarhum=request.POST.get("inputAlmarhum"),
            suami=request.POST.get("inputSuami"),
            istri=request.POST.get("inputIstri"),
            jumlahanak=request.POST.get("inputJumlahanak"),
            tanggalmeninggal=request.POST.get("inputTanggalmeninggal"),
            bulanmeninggal=request.POST.get("inputBulanmeninggal"),
            tahunmeninggal=request.POST.get("inputTahunmeninggal"),
            nama1=request.POST.get("inputNama1"),
            ttl1=request.POST.get("inputTtl1"),
            alamat1=request.POST.get("inputAlamat1"),
            nama2=request.POST.get("inputNama2"),
            ttl2=request.POST.get("inputTtl2"),
            alamat2=request.POST.get("inputAlamat2"),
            nama3=request.POST.get("inputNama3"),
            ttl3=request.POST.get("inputTtl3"),
            alamat3=request.POST.get("inputAlamat3"),
            nama4=request.POST.get("inputNama4"),
            ttl4=request.POST.get("inputTtl4"),
            alamat4=request.POST.get("inputAlamat4"),
            skkematian=skkematian_url,
            scanktpkkahliwaris1=scanktpkkahliwaris1_url,
            scanktpkkahliwaris2=scanktpkkahliwaris2_url,
            scanktpkkahliwaris3=scanktpkkahliwaris3_url,
            scanktpkkahliwaris4=scanktpkkahliwaris4_url,
            scanktpsaksi1=scanktpsaksi1_url,
            scanktpsaksi2=scanktpsaksi2_url,
        )
    
        return redirect('suketahliwaris')
    
    context = {
        "suket": suket,
        'private': private,
    }
    
    return render(request, template_name, context)

@login_required
def edit_suketahliwaris(request, id):
    template_name = "backend/suketahliwaris.html"
    
    suket_id = SuketAhliWaris.objects.get(id=id)
    
    if request.method == "POST":
        fs = FileSystemStorage()

        skkematian_file = request.FILES.get("skkematian")
        if skkematian_file:
            skkematian_filename = skkematian_file.name.replace(" ", "_")
            skkematian_filename = fs.save(skkematian_file.name, skkematian_file)
            suket_id.skkematian = fs.url(skkematian_filename)

        scanktpkkahliwaris1_file = request.FILES.get("scanktpkkahliwaris1")
        if scanktpkkahliwaris1_file:
            scanktpkkahliwaris1_filename = scanktpkkahliwaris1_file.name.replace(" ", "_")
            scanktpkkahliwaris1_filename = fs.save(scanktpkkahliwaris1_file.name, scanktpkkahliwaris1_file)
            suket_id.scanktpkkahliwaris1 = fs.url(scanktpkkahliwaris1_filename)

        scanktpkkahliwaris2_file = request.FILES.get("scanktpkkahliwaris2")
        if scanktpkkahliwaris2_file:
            scanktpkkahliwaris2_filename = scanktpkkahliwaris2_file.name.replace(" ", "_")
            scanktpkkahliwaris2_filename = fs.save(scanktpkkahliwaris2_file.name, scanktpkkahliwaris2_file)
            suket_id.scanktpkkahliwaris2 = fs.url(scanktpkkahliwaris2_filename)

        scanktpkkahliwaris3_file = request.FILES.get("scanktpkkahliwaris3")
        if scanktpkkahliwaris3_file:
            scanktpkkahliwaris3_filename = scanktpkkahliwaris3_file.name.replace(" ", "_")
            scanktpkkahliwaris3_filename = fs.save(scanktpkkahliwaris3_file.name, scanktpkkahliwaris3_file)
            suket_id.scanktpkkahliwaris3 = fs.url(scanktpkkahliwaris3_filename)

        scanktpkkahliwaris4_file = request.FILES.get("scanktpkkahliwaris4")
        if scanktpkkahliwaris4_file:
            scanktpkkahliwaris4_filename = scanktpkkahliwaris4_file.name.replace(" ", "_")
            scanktpkkahliwaris4_filename = fs.save(scanktpkkahliwaris4_file.name, scanktpkkahliwaris4_file)
            suket_id.scanktpkkahliwaris4 = fs.url(scanktpkkahliwaris4_filename)

        scanktpsaksi1_file = request.FILES.get("scanktpsaksi1")
        if scanktpsaksi1_file:
            scanktpsaksi1_filename = scanktpsaksi1_file.name.replace(" ", "_")
            scanktpsaksi1_filename = fs.save(scanktpsaksi1_file.name, scanktpsaksi1_file)
            suket_id.scanktpsaksi1 = fs.url(scanktpsaksi1_filename)

        scanktpsaksi2_file = request.FILES.get("scanktpsaksi2")
        if scanktpsaksi2_file:
            scanktpsaksi2_filename = scanktpsaksi2_file.name.replace(" ", "_")
            scanktpsaksi2_filename = fs.save(scanktpsaksi2_file.name, scanktpsaksi2_file)
            suket_id.scanktpsaksi2 = fs.url(scanktpsaksi2_filename)

        # Mengupdate data lainnya
        suket_id.penulis = request.user
        suket_id.almarhum=request.POST.get("inputAlmarhum")
        suket_id.suami=request.POST.get("inputSuami")
        suket_id.istri=request.POST.get("inputIstri")
        suket_id.jumlahanak=request.POST.get("inputJumlahanak")
        suket_id.tanggalmeninggal=request.POST.get("inputTanggalmeninggal")
        suket_id.bulanmeninggal=request.POST.get("inputBulanmeninggal")
        suket_id.tahunmeninggal=request.POST.get("inputTahunmeninggal")
        suket_id.nama1 = request.POST.get("inputNama1")
        suket_id.ttl1 = request.POST.get("inputTtl1")
        suket_id.alamat1 = request.POST.get("inputAlamat1")
        suket_id.nama2 = request.POST.get("inputNama2")
        suket_id.ttl2 = request.POST.get("inputTtl2")
        suket_id.alamat2 = request.POST.get("inputAlamat2")
        suket_id.nama3 = request.POST.get("inputNama3")
        suket_id.ttl3 = request.POST.get("inputTtl3")
        suket_id.alamat3 = request.POST.get("inputAlamat3")
        suket_id.nama4 = request.POST.get("inputNama4")
        suket_id.ttl4 = request.POST.get("inputTtl4")
        suket_id.alamat4 = request.POST.get("inputAlamat4")
        suket_id.date = timezone.now()
        suket_id.status = 'review'

        suket_id.save()
        
        return redirect('suketahliwaris')
    
    context = {
        "value": suket_id
    }
    
    return render(request, template_name, context)

@login_required
def setujui_suketahliwaris(request, id):
    if request.user.is_superuser:
        suket = get_object_or_404(SuketAhliWaris, id=id)
        suket.status = 'approved'  # Mengubah status menjadi Disetujui
        suket.save()
    return redirect('suketahliwaris')  # Redirect ke halaman list Suket Ahli Waris

@login_required
def tolak_suketahliwaris(request, id):
    if request.user.is_superuser:
        suket = get_object_or_404(SuketAhliWaris, id=id)
        suket.status = 'rejected'  # Mengubah status menjadi Ditolak
        suket.save()
    return redirect('suketahliwaris')  # Redirect ke halaman list Suket Ahli Waris

@login_required
def delete_suketahliwaris(request, id):
    # Menghapus data berdasarkan id
    SuketAhliWaris.objects.get(id=id).delete()
    
    return redirect('suketahliwaris')

@login_required
def print_suketahliwaris(request, id):
    # Mengambil data surat
    
    template_name= "surat/surat-keterangan-ahli-waris.html"
    surat = get_object_or_404(SuketAhliWaris, id=id)

    # Mengisi template dengan data surat
    context = {
        'almarhum': surat.almarhum,
        'suami': surat.suami,
        'istri': surat.istri,
        'jumlahanak': surat.jumlahanak,
        'tanggalmeninggal': surat.tanggalmeninggal,
        'bulanmeninggal': surat.bulanmeninggal,
        'tahunmeninggal': surat.tahunmeninggal,
        'nama1': surat.nama1,
        'ttl1': surat.ttl1,
        'alamat1': surat.alamat1,
        'nama2': surat.nama2,
        'ttl2': surat.ttl2,
        'alamat2': surat.alamat2,
        'nama3': surat.nama3,
        'ttl3': surat.ttl3,
        'alamat3': surat.alamat3,
        'nama4': surat.nama4,
        'ttl4': surat.ttl4,
        'alamat4': surat.alamat4,
        'date': surat.date,
    }
    
    return render(request,template_name, context)

@login_required
def detail_suketahliwaris(request, id):
    template_name = "backend/detail_suketahliwaris.html"  # Template untuk halaman detail
    
    # Mengambil objek SuketAhliWaris berdasarkan ID
    suket = get_object_or_404(SuketAhliWaris, id=id)
    
    # Mengirim data ke template
    context = {
        'suket': suket,
    }
    
    return render(request, template_name, context)

@login_required
def suketMTQ(request):
    template_name = "backend/suketMTQ.html"
    
    suket = SuketMTQ.objects.all()
    private = SuketMTQ.objects.filter(penulis=request.user)
    
    if request.method == "POST":
        fs = FileSystemStorage()

        # Mengambil file yang di-upload
        file_upload = request.FILES.get("file")
        file_url = None

        if file_upload:
            # Mengubah nama file yang mengandung spasi menjadi underscore
            filename = file_upload.name.replace(" ", "_")
            saved_filename = fs.save(filename, file_upload)
            file_url = fs.url(saved_filename)

        # Membuat SuketMTQ baru
        SuketMTQ.objects.create(
            penulis=request.user,
            nama=request.POST.get("inputNama"),
            jenis_kelamin=request.POST.get("inputjk"),
            ttl=request.POST.get("inputTtl"),
            suku=request.POST.get("inputSuku"),
            agama=request.POST.get("inputAgama"),
            alamat=request.POST.get("inputAlamat"),
            pekerjaan=request.POST.get("inputPekerjaan"),
            dusun=request.POST.get("inputDusun"),
            tahunmenetap=request.POST.get("inputTahunMenetap"),
            keperluan=request.POST.get("inputKeperluan"),
            # file_url=file_url  # Menyimpan URL file jika diperlukan
        )
    
        return redirect('suketMTQ')
    
    context = {
        "suket": suket,
        'private': private
    }
    
    return render(request, template_name, context)

@login_required
def edit_suketMTQ(request, id):
    template_name = "backend/suketMTQ.html"
    suket_id = SuketMTQ.objects.get(id=id)
    
    if request.method == "POST":
        fs = FileSystemStorage()

        # Mengambil file yang di-upload
        file_upload = request.FILES.get("file")
        if file_upload:
            # Mengubah nama file yang mengandung spasi menjadi underscore
            filename = file_upload.name.replace(" ", "_")
            saved_filename = fs.save(filename, file_upload)
            suket_id.file_url = fs.url(saved_filename)

        # Mengedit data SuketMTQ
        suket_id.penulis = request.user
        suket_id.nama = request.POST.get("inputNama")
        suket_id.jenis_kelamin = request.POST.get("inputjk")
        suket_id.ttl = request.POST.get("inputTtl")
        suket_id.suku = request.POST.get("inputSuku")
        suket_id.agama = request.POST.get("inputAgama")
        suket_id.alamat = request.POST.get("inputAlamat")
        suket_id.pekerjaan = request.POST.get("inputPekerjaan")
        suket_id.dusun = request.POST.get("inputDusun")
        suket_id.tahunmenetap = request.POST.get("inputTahunMenetap")
        suket_id.keperluan = request.POST.get("inputKeperluan")
        suket_id.date = timezone.now()
        suket_id.status = 'review'
        
        suket_id.save()
        
        return redirect('suketMTQ')
    
    context = {
        "value": suket_id
    }
    
    return render(request, template_name, context)

@login_required
def setujui_suketmtq(request, id):
    if request.user.is_superuser:
        suket = get_object_or_404(SuketMTQ, id=id)
        suket.status = 'approved'  # Mengubah status menjadi Disetujui
        suket.save()
    return redirect('suketMTQ')
# Redirect ke halaman list Suket MTQ
@login_required
def tolak_suketmtq(request, id):
    if request.user.is_superuser:
        suket = get_object_or_404(SuketMTQ, id=id)
        suket.status = 'rejected'  # Mengubah status menjadi Ditolak
        suket.save()
    return redirect('suketMTQ')  # Redirect ke halaman list Suket MTQ

@login_required
def delete_suketMTQ(request, id):
    # Menghapus data berdasarkan id
    SuketMTQ.objects.get(id=id).delete()
    
    
    return redirect('suketMTQ')

@login_required
def print_suketMTQ(request, id):
    # Mengambil data surat
    
    template_name= "surat/surat-keterangan-domisili-mtq-baru.html"
    surat = get_object_or_404(SuketMTQ, id=id)

    # Mengisi template dengan data surat
    context = {
        'nama': surat.nama,
        'ttl': surat.ttl,
        'jenis_kelamin': surat.jenis_kelamin,
        'suku': surat.suku,
        'agama': surat.agama,
        'pekerjaan': surat.pekerjaan,
        'alamat': surat.alamat,
        'dusun': surat.dusun,
        'tahunmenetap': surat.tahunmenetap,
        'keperluan': surat.keperluan,
        'date': surat.date,
    }
    
    return render(request,template_name, context)

@login_required
def detail_suketmtq(request, id):
    template_name = "backend/detail_suketmtq.html"  # Template untuk halaman detail
    
    # Mengambil objek SuketMTQ berdasarkan ID
    suket = get_object_or_404(SuketMTQ, id=id)
    
    # Mengirim data ke template
    context = {
        'suket': suket,
    }
    
    return render(request, template_name, context)

@login_required
def suketkehilangan(request):
    template_name = "backend/suketkehilangan.html"
    
    suket = SuketKehilangan.objects.all()
    private =SuketKehilangan.objects.filter(penulis=request.user)
    
    if request.method == "POST":
        # Membuat SuketKehilangan baru
        SuketKehilangan.objects.create(
            penulis=request.user,
            nama=request.POST.get("inputNama"),
            jenis_kelamin=request.POST.get("inputjk"),
            umur=request.POST.get("inputUmur"),
            alamat=request.POST.get("inputAlamat"),
            pekerjaan=request.POST.get("inputPekerjaan"),
            barang1=request.POST.get("inputBarang1"),
            barang2=request.POST.get("inputBarang2"),
            barang3=request.POST.get("inputBarang3"),
            tempat1=request.POST.get("inputTempat1"),
            tempat2=request.POST.get("inputTempat2"),
            harikehilangan=request.POST.get("inputHariKehilangan"),
        )
    
        return redirect('suketkehilangan')
    
    context = {
        "suket": suket,
        'private':private
    }
    
    return render(request, template_name, context)

@login_required
def edit_suketkehilangan(request, id):
    template_name = "backend/suketkehilangan.html"
    
    suket_id = SuketKehilangan.objects.get(id=id)
    
    if request.method == "POST":
        # Mengedit data SuketKehilangan
        penulis = request.user
        nama = request.POST.get("inputNama")
        jenis_kelamin = request.POST.get("inputjk")
        umur = request.POST.get("inputUmur")
        alamat = request.POST.get("inputAlamat")
        pekerjaan = request.POST.get("inputPekerjaan")
        barang1 = request.POST.get("inputBarang1")
        barang2 = request.POST.get("inputBarang2")
        barang3 = request.POST.get("inputBarang3")
        tempat1 = request.POST.get("inputTempat1")
        tempat2 = request.POST.get("inputTempat2")
        harikehilangan=request.POST.get("inputHariKehilangan")
        
        suket_id.penulis = penulis
        suket_id.nama = nama
        suket_id.jenis_kelamin = jenis_kelamin
        suket_id.umur = umur
        suket_id.alamat = alamat
        suket_id.pekerjaan = pekerjaan
        suket_id.barang1 = barang1
        suket_id.barang2 = barang2
        suket_id.barang3 = barang3
        suket_id.tempat1 = tempat1
        suket_id.tempat2 = tempat2
        suket_id.harikehilangan = harikehilangan
        suket_id.date = timezone.now()  # Mengupdate tanggal saat edit
        suket_id.status='review'
        
        suket_id.save()
        
        return redirect('suketkehilangan')
    
    context = {
        "value": suket_id
    }
    
    return render(request, template_name, context)

@login_required
def setujui_suketkehilangan(request, id):
    if request.user.is_superuser:
        suket = get_object_or_404(SuketKehilangan, id=id)
        suket.status = 'approved'  # Mengubah status menjadi Disetujui
        suket.save()
    return redirect('suketkehilangan')  # Redirect ke halaman list Suket Kehilangan

@login_required
def tolak_suketkehilangan(request, id):
    if request.user.is_superuser:
        suket = get_object_or_404(SuketKehilangan, id=id)
        suket.status = 'rejected'  # Mengubah status menjadi Ditolak
        suket.save()
    return redirect('suketkehilangan')  # Redirect ke halaman list Suket Kehilangan

@login_required
def delete_suketkehilangan(request, id):
    # Menghapus data berdasarkan id
    SuketKehilangan.objects.get(id=id).delete()
    
    return redirect('suketkehilangan')

@login_required
def print_suketkehilangan(request, id):
    # Mengambil data surat
    
    template_name= "surat/surat-keterangan-kehilangan.html"
    surat = get_object_or_404(SuketKehilangan, id=id)

    # Mengisi template dengan data surat
    context = {
        'nama': surat.nama,
        'jenis_kelamin': surat.jenis_kelamin,
        'umur': surat.umur,
        'pekerjaan': surat.pekerjaan,
        'alamat': surat.alamat,
        'barang1': surat.barang1,
        'barang2': surat.barang2,
        'barang3': surat.barang3,
        'tempat1': surat.tempat1,
        'tempat2': surat.tempat2,
        'harikehilangan': surat.harikehilangan,
        'date': surat.date,
    }
    
    return render(request,template_name, context)

@login_required
def detail_suketkehilangan(request, id):
    template_name = "backend/detail_suketkehilangan.html"  # Template untuk halaman detail
    
    # Mengambil objek SuketKehilangan berdasarkan ID
    suket = get_object_or_404(SuketKehilangan, id=id)
    
    # Mengirim data ke template
    context = {
        'suket': suket,
    }
    
    return render(request, template_name, context)

@login_required
def suketkelahiran(request):
    template_name = "backend/suketkelahiran.html"
    
    suket = SuketKelahiran.objects.all()
    private = SuketKelahiran.objects.filter(penulis=request.user)
    
    if request.method == "POST":
        fs = FileSystemStorage()

        def save_file_with_underscore(file):
            if file:
                # Mengganti spasi pada nama file dengan underscore
                new_filename = file.name.replace(" ", "_")
                return fs.url(fs.save(new_filename, file))
            return None

        # Menyimpan file-file yang di-upload dengan mengganti spasi menjadi underscore
        kkb_url = save_file_with_underscore(request.FILES.get("kkb"))
        scanfcbnb_url = save_file_with_underscore(request.FILES.get("scanfcbnb"))
        scanfcktportub_url = save_file_with_underscore(request.FILES.get("scanfcktportub"))
        scanfcktpsaksib1_url = save_file_with_underscore(request.FILES.get("scanfcktpsaksib1"))
        scanfcktpsaksib2_url = save_file_with_underscore(request.FILES.get("scanfcktpsaksib2"))
        kkd_url = save_file_with_underscore(request.FILES.get("kkd"))
        kk_ktportud_url = save_file_with_underscore(request.FILES.get("kk_ktportud"))
        scanfcktpsaksid1_url = save_file_with_underscore(request.FILES.get("scanfcktpsaksid1"))
        scanfcktpsaksid2_url = save_file_with_underscore(request.FILES.get("scanfcktpsaksid2"))

        # Menyimpan data SuketKelahiran
        SuketKelahiran.objects.create(
            penulis=request.user,
            namab=request.POST.get("inputNamaB"),
            jenis_kelaminb=request.POST.get("inputJenisKelaminB"),
            tanggal_lahirb=request.POST.get("inputTanggalLahirB"),
            tempat_lahirb=request.POST.get("inputTempatLahirB"),
            agamab=request.POST.get("inputAgamaB"),
            alamatb=request.POST.get("inputAlamatB"),
            anakke=request.POST.get("inputAnakKe"),
            namaa=request.POST.get("inputNamaA"),
            umura=request.POST.get("inputUmurA"),
            pekerjaana=request.POST.get("inputPekerjaanA"),
            alamata=request.POST.get("inputAlamatA"),
            namai=request.POST.get("inputNamaI"),
            umuri=request.POST.get("inputUmurI"),
            pekerjaani=request.POST.get("inputPekerjaanI"),
            alamati=request.POST.get("inputAlamatI"),
            persyaratan=request.POST.get("inputPersyaratan"),
            kkb=kkb_url,
            scanfcbnb=scanfcbnb_url,
            scanfcktportub=scanfcktportub_url,
            scanfcktpsaksib1=scanfcktpsaksib1_url,
            scanfcktpsaksib2=scanfcktpsaksib2_url,
            kkd=kkd_url,
            kk_ktportud=kk_ktportud_url,
            scanfcktpsaksid1=scanfcktpsaksid1_url,
            scanfcktpsaksid2=scanfcktpsaksid2_url
        )
    
        return redirect('suketkelahiran')
    
    context = {
        "suket": suket,
        'private': private,
    }
    
    return render(request, template_name, context)


@login_required
def edit_suketkelahiran(request, id):
    template_name = "backend/suketkelahiran.html"
    
    suket_id = SuketKelahiran.objects.get(id=id)
    fs = FileSystemStorage()

    def save_file_with_underscore(file):
        if file:
            # Mengganti spasi pada nama file dengan underscore
            new_filename = file.name.replace(" ", "_")
            return fs.url(fs.save(new_filename, file))
        return None
    
    if request.method == "POST":
        # Menyimpan file baru jika ada, dengan mengganti spasi menjadi underscore
        kkb_url = save_file_with_underscore(request.FILES.get("kkb"))
        if kkb_url:
            suket_id.kkb = kkb_url
        
        scanfcbnb_url = save_file_with_underscore(request.FILES.get("scanfcbnb"))
        if scanfcbnb_url:
            suket_id.scanfcbnb = scanfcbnb_url

        scanfcktportub_url = save_file_with_underscore(request.FILES.get("scanfcktportub"))
        if scanfcktportub_url:
            suket_id.scanfcktportub = scanfcktportub_url

        scanfcktpsaksib1_url = save_file_with_underscore(request.FILES.get("scanfcktpsaksib1"))
        if scanfcktpsaksib1_url:
            suket_id.scanfcktpsaksib1 = scanfcktpsaksib1_url

        scanfcktpsaksib2_url = save_file_with_underscore(request.FILES.get("scanfcktpsaksib2"))
        if scanfcktpsaksib2_url:
            suket_id.scanfcktpsaksib2 = scanfcktpsaksib2_url

        kkd_url = save_file_with_underscore(request.FILES.get("kkd"))
        if kkd_url:
            suket_id.kkd = kkd_url

        kk_ktportud_url = save_file_with_underscore(request.FILES.get("kk_ktportud"))
        if kk_ktportud_url:
            suket_id.kk_ktportud = kk_ktportud_url

        scanfcktpsaksid1_url = save_file_with_underscore(request.FILES.get("scanfcktpsaksid1"))
        if scanfcktpsaksid1_url:
            suket_id.scanfcktpsaksid1 = scanfcktpsaksid1_url

        scanfcktpsaksid2_url = save_file_with_underscore(request.FILES.get("scanfcktpsaksid2"))
        if scanfcktpsaksid2_url:
            suket_id.scanfcktpsaksid2 = scanfcktpsaksid2_url

        # Mengedit data SuketKelahiran
        suket_id.penulis = request.user
        suket_id.namab = request.POST.get("inputNamaB")
        suket_id.jenis_kelaminb = request.POST.get("inputJenisKelaminB")
        suket_id.tanggal_lahirb = request.POST.get("inputTanggalLahirB")
        suket_id.tempat_lahirb = request.POST.get("inputTempatLahirB")
        suket_id.agamab = request.POST.get("inputAgamaB")
        suket_id.alamatb = request.POST.get("inputAlamatB")
        suket_id.anakke = request.POST.get("inputAnakKe")
        suket_id.namaa = request.POST.get("inputNamaA")
        suket_id.umura = request.POST.get("inputUmurA")
        suket_id.pekerjaana = request.POST.get("inputPekerjaanA")
        suket_id.alamata = request.POST.get("inputAlamatA")
        suket_id.namai = request.POST.get("inputNamaI")
        suket_id.umuri = request.POST.get("inputUmurI")
        suket_id.pekerjaani = request.POST.get("inputPekerjaanI")
        suket_id.alamati = request.POST.get("inputAlamatI")
        suket_id.persyaratan = request.POST.get("inputPersyaratan")
        suket_id.date = timezone.now()  # Mengupdate tanggal saat edit
        suket_id.status = 'review'
        
        suket_id.save()
        
        return redirect('suketkelahiran')
    
    context = {
        "value": suket_id
    }
    
    return render(request, template_name, context)

@login_required
def setujui_suketkelahiran(request, id):
    if request.user.is_superuser:
        suket = get_object_or_404(SuketKelahiran, id=id)
        suket.status = 'approved'  # Mengubah status menjadi Disetujui
        suket.save()
    return redirect('suketkelahiran')  # Redirect ke halaman list Suket Kelahiran

@login_required
def tolak_suketkelahiran(request, id):
    if request.user.is_superuser:
        suket = get_object_or_404(SuketKelahiran, id=id)
        suket.status = 'rejected'  # Mengubah status menjadi Ditolak
        suket.save()
    return redirect('suketkelahiran')  # Redirect ke halaman list Suket Kelahiran

@login_required
def delete_suketkelahiran(request, id):
    SuketKelahiran.objects.get(id=id).delete()
    
    return redirect('suketkelahiran')

@login_required
def print_suketkelahiran(request, id):
    # Mengambil data surat
    
    template_name= "surat/surat-keterangan-kelahiran.html"
    surat = get_object_or_404(SuketKelahiran, id=id)

    # Mengisi template dengan data surat
    context = {
        'namab': surat.namab,
        'jenis_kelaminb': surat.jenis_kelaminb,
        'tanggal_lahirb': surat.tanggal_lahirb,
        'tempat_lahirb': surat.tempat_lahirb,
        'agamab': surat.agamab,
        'alamatb': surat.alamatb,
        'anakke': surat.anakke,
        'namaa': surat.namaa,
        'umura': surat.umura,
        'pekerjaana': surat.pekerjaana,
        'alamata': surat.alamata,
        'namai': surat.namai,
        'umuri': surat.umuri,
        'pekerjaani': surat.pekerjaani,
        'alamati': surat.alamati,
        'persyaratan': surat.persyaratan,
        'date': surat.date,
    }
    
    return render(request,template_name, context)

@login_required
def detail_suketkelahiran(request, id):
    template_name = "backend/detail_suketkelahiran.html"  # Template untuk halaman detail
    
    # Mengambil objek SuketKelahiran berdasarkan ID
    suket = get_object_or_404(SuketKelahiran, id=id)
    
    # Mengirim data ke template
    context = {
        'suket': suket,
    }
    
    return render(request, template_name, context)

@login_required
def suketkematian(request):
    template_name = "backend/suketkematian.html"
    
    suket = SuketKematian.objects.all()
    private = SuketKematian.objects.filter(penulis=request.user)

    def save_file_with_underscore(file):
        if file:
            new_filename = file.name.replace(" ", "_")  # Mengganti spasi dengan underscore
            return fs.url(fs.save(new_filename, file))
        return None
    
    if request.method == "POST":
        fs = FileSystemStorage()
        
        myfile_pengantar = request.FILES.get("pengantarrt")
        myfile_scankk = request.FILES.get("scankk")

        # Jika ada file pengantar RT yang di-upload
        url_pengantar = save_file_with_underscore(myfile_pengantar)
        
        # Jika ada file scan KK yang di-upload
        url_scankk = save_file_with_underscore(myfile_scankk)
        
        # Membuat objek SuketKematian baru
        SuketKematian.objects.create(
            penulis=request.user,
            nama=request.POST.get("inputNama"),
            nip=request.POST.get("inputNIP"),
            jabatan=request.POST.get("inputJabatan"),
            nokk=request.POST.get("inputNoKK"),
            namaalm=request.POST.get("inputNamaAlm"),
            nikalm=request.POST.get("inputNIKAlm"),
            ttlalm=request.POST.get("inputTTLAlm"),
            agamaalm=request.POST.get("inputAgamaAlm"),
            anakkealm=request.POST.get("inputAnakkeAlm"),
            ibualm=request.POST.get("inputIbuAlm"),
            ayahalm=request.POST.get("inputAyahAlm"),
            pekerjaanalm=request.POST.get("inputPekerjaanAlm"),
            kewarganegaraanalm=request.POST.get("inputKewarganegaraanAlm"),
            alamatalm=request.POST.get("inputAlamatAlm"),
            tanggal_kematian=request.POST.get("inputTanggalKematian"),
            jam_kematian=request.POST.get("inputJamKematian"),
            tempat_kematian=request.POST.get("inputTempatKematian"),
            penyebab_kematian=request.POST.get("inputPenyebabKematian"),
            tmptmakam=request.POST.get("inputTempatMakam"),
            tanggal_pmkn=request.POST.get("inputTanggalPemakaman"),
            jam_pmkn=request.POST.get("inputJamPemakaman"),
            pengantarrt=url_pengantar,
            scankk=url_scankk,
        )
    
        return redirect('suketkematian')
    
    context = {
        "suket": suket,
        'private': private 
    }
    
    return render(request, template_name, context)

@login_required
def edit_suketkematian(request, id):
    template_name = "backend/suketkematian.html"
    
    suket_id = SuketKematian.objects.get(id=id)

    def save_file_with_underscore(file):
        if file:
            new_filename = file.name.replace(" ", "_")  # Mengganti spasi dengan underscore
            return fs.url(fs.save(new_filename, file))
        return None
    
    if request.method == "POST":
        penulis = request.user
        nama = request.POST.get("inputNama")
        nip = request.POST.get("inputNIP")
        jabatan = request.POST.get("inputJabatan")
        nokk = request.POST.get("inputNoKK")
        namaalm = request.POST.get("inputNamaAlm")
        nikalm = request.POST.get("inputNIKAlm")
        ttlalm = request.POST.get("inputTTLAlm")
        agamaalm = request.POST.get("inputAgamaAlm")
        anakkealm = request.POST.get("inputAnakkeAlm")
        ibualm = request.POST.get("inputIbuAlm")
        ayahalm = request.POST.get("inputAyahAlm")
        pekerjaanalm = request.POST.get("inputPekerjaanAlm")
        kewarganegaraanalm = request.POST.get("inputKewarganegaraanAlm")
        alamatalm = request.POST.get("inputAlamatAlm")
        tanggal_kematian = request.POST.get("inputTanggalKematian")
        jam_kematian = request.POST.get("inputJamKematian")
        tempat_kematian = request.POST.get("inputTempatKematian")
        penyebab_kematian = request.POST.get("inputPenyebabKematian")
        tmptmakam = request.POST.get("inputTempatMakam")
        tanggal_pmkn = request.POST.get("inputTanggalPemakaman")
        jam_pmkn = request.POST.get("inputJamPemakaman")

        fs = FileSystemStorage()

        # Mengecek apakah ada file baru yang di-upload
        myfile_pengantar = request.FILES.get("pengantarrt")
        myfile_scankk = request.FILES.get("scankk")

        # Jika ada file pengantar RT baru yang di-upload
        if myfile_pengantar:
            suket_id.pengantarrt = save_file_with_underscore(myfile_pengantar)
        
        # Jika ada file scan KK baru yang di-upload
        if myfile_scankk:
            suket_id.scankk = save_file_with_underscore(myfile_scankk)
        
        # Update data di objek suket_id
        suket_id.penulis = penulis
        suket_id.nama = nama
        suket_id.nip = nip
        suket_id.jabatan = jabatan
        suket_id.nokk = nokk
        suket_id.namaalm = namaalm
        suket_id.nikalm = nikalm
        suket_id.ttlalm = ttlalm
        suket_id.agamaalm = agamaalm
        suket_id.anakkealm = anakkealm
        suket_id.ibualm = ibualm
        suket_id.ayahalm = ayahalm
        suket_id.pekerjaanalm = pekerjaanalm
        suket_id.kewarganegaraanalm = kewarganegaraanalm
        suket_id.alamatalm = alamatalm
        suket_id.tanggal_kematian = tanggal_kematian
        suket_id.jam_kematian = jam_kematian
        suket_id.tempat_kematian = tempat_kematian
        suket_id.penyebab_kematian = penyebab_kematian
        suket_id.tmptmakam = tmptmakam
        suket_id.tanggal_pmkn = tanggal_pmkn
        suket_id.jam_pmkn = jam_pmkn
        suket_id.date = timezone.now()
        suket_id.status = 'review'

        suket_id.save()
        
        return redirect('suketkematian')
    
    context = {
        "value": suket_id
    }
    
    return render(request, template_name, context)

@login_required
def setujui_suketkematian(request, id):
    if request.user.is_superuser:
        suket = get_object_or_404(SuketKematian, id=id)
        suket.status = 'approved'  # Mengubah status menjadi Disetujui
        suket.save()
    return redirect('suketkematian')  # Redirect ke halaman list Suket Kematian

@login_required
def tolak_suketkematian(request, id):
    if request.user.is_superuser:
        suket = get_object_or_404(SuketKematian, id=id)
        suket.status = 'rejected'  # Mengubah status menjadi Ditolak
        suket.save()
    return redirect('suketkematian')  # Redirect ke halaman list Suket Kematian

@login_required
def delete_suketkematian(request, id):
    SuketKematian.objects.get(id=id).delete()
    return redirect('suketkematian')

@login_required
def print_suketkematian(request, id):
    # Mengambil data surat
    
    template_name= "surat/surat-keterangan-kematian.html"
    surat = get_object_or_404(SuketKematian, id=id)

    # Mengisi template dengan data surat
    context = {
        'nama': surat.nama,
        'nip': surat.nip,
        'jabatan': surat.jabatan,
        'nokk': surat.nokk,
        'namaalm': surat.namaalm,
        'nikalm': surat.nikalm,
        'ttlalm': surat.ttlalm,
        'agamaalm': surat.agamaalm,
        'anakkealm': surat.anakkealm,
        'ibualm': surat.ibualm,
        'ayahalm': surat.ayahalm,
        'pekerjaanalm': surat.pekerjaanalm,
        'kewarganegaraanalm': surat.kewarganegaraanalm,
        'alamatalm': surat.alamatalm,
        'tanggal_kematian': surat.tanggal_kematian,
        'jam_kematian': surat.jam_kematian,
        'tempat_kematian': surat.tempat_kematian,
        'penyebab_kematian': surat.penyebab_kematian,
        'tmptmakam': surat.tmptmakam,
        'tanggal_pmkn': surat.tanggal_pmkn,
        'jam_pmkn': surat.jam_pmkn,
        'date': surat.date,
    }
    
    return render(request,template_name, context)

@login_required
def detail_suketkematian(request, id):
    template_name = "backend/detail_suketkematian.html"  # Template untuk halaman detail
    
    # Mengambil objek SuketKematian berdasarkan ID
    suket = get_object_or_404(SuketKematian, id=id)
    
    # Mengirim data ke template
    context = {
        'suket': suket,
    }
    
    return render(request, template_name, context)

@login_required
def suketpenghasilantidaktetap(request):
    template_name = "backend/suketpenghasilantidaktetap.html"
    
    suket = SuketPenghasilanTidakTetap.objects.all()
    private = SuketPenghasilanTidakTetap.objects.filter(penulis=request.user)

    def save_file_with_underscore(file):
        if file:
            new_filename = file.name.replace(" ", "_")  # Mengganti spasi dengan underscore
            return fs.url(fs.save(new_filename, file))
        return None

    if request.method == "POST":
        fs = FileSystemStorage()

        myfile_pengantar = request.FILES.get("pengantarrt")
        myfile_scankk = request.FILES.get("scankk")

        # Jika ada file pengantar RT yang di-upload
        url_pengantar = save_file_with_underscore(myfile_pengantar)
        
        # Jika ada file scan KK yang di-upload
        url_scankk = save_file_with_underscore(myfile_scankk)
        
        # Membuat objek SuketPenghasilanTidakTetap baru
        SuketPenghasilanTidakTetap.objects.create(
            penulis=request.user,
            nama=request.POST.get("inputNama"),
            umur=request.POST.get("inputUmur"),
            pekerjaan=request.POST.get("inputPekerjaan"),
            alamat=request.POST.get("inputAlamat"),
            penghasilan=request.POST.get("inputPenghasilan"),
            pengantarrt=url_pengantar,
            scankk=url_scankk,
        )
    
        return redirect('suketpenghasilantidaktetap')
    
    context = {
        "suket": suket,
        'private': private
    }
    
    return render(request, template_name, context)

@login_required
def edit_suketpenghasilantidaktetap(request, id):
    template_name = "backend/suketpenghasilantidaktetap.html"
    
    suket_id = SuketPenghasilanTidakTetap.objects.get(id=id)

    def save_file_with_underscore(file):
        if file:
            new_filename = file.name.replace(" ", "_")  # Mengganti spasi dengan underscore
            return fs.url(fs.save(new_filename, file))
        return None
    
    if request.method == "POST":
        penulis = request.user
        nama = request.POST.get("inputNama")
        umur = request.POST.get("inputUmur")
        pekerjaan = request.POST.get("inputPekerjaan")
        alamat = request.POST.get("inputAlamat")
        penghasilan = request.POST.get("inputPenghasilan")

        fs = FileSystemStorage()

        # Mengecek apakah ada file baru yang di-upload
        myfile_pengantar = request.FILES.get("pengantarrt")
        myfile_scankk = request.FILES.get("scankk")

        # Jika ada file pengantar RT baru yang di-upload
        if myfile_pengantar:
            suket_id.pengantarrt = save_file_with_underscore(myfile_pengantar)
        
        # Jika ada file scan KK baru yang di-upload
        if myfile_scankk:
            suket_id.scankk = save_file_with_underscore(myfile_scankk)
        
        # Update data di objek suket_id
        suket_id.penulis = penulis
        suket_id.nama = nama
        suket_id.umur = umur
        suket_id.pekerjaan = pekerjaan
        suket_id.alamat = alamat
        suket_id.penghasilan = penghasilan
        suket_id.date = timezone.now()
        suket_id.status = 'review'

        suket_id.save()
        
        return redirect('suketpenghasilantidaktetap')
    
    context = {
        "value": suket_id
    }
    
    return render(request, template_name, context)

@login_required
def setujui_suketpenghasilantidaktetap(request, id):
    if request.user.is_superuser:
        suket = get_object_or_404(SuketPenghasilanTidakTetap, id=id)
        suket.status = 'approved'  # Mengubah status menjadi Disetujui
        suket.save()
    return redirect('suketpenghasilantidaktetap') 
# Redirect ke halaman list Suket Penghasilan Tidak Tetap
@login_required
def tolak_suketpenghasilantidaktetap(request, id):
    if request.user.is_superuser:
        suket = get_object_or_404(SuketPenghasilanTidakTetap, id=id)
        suket.status = 'rejected'  # Mengubah status menjadi Ditolak
        suket.save()
    return redirect('suketpenghasilantidaktetap')  # Redirect ke halaman list Suket Penghasilan Tidak Tetap

@login_required
def delete_suketpenghasilantidaktetap(request, id):
    SuketPenghasilanTidakTetap.objects.get(id=id).delete()
    return redirect('suketpenghasilantidaktetap')

@login_required
def print_suketpenghasilantidaktetap(request, id):
    # Mengambil data surat
    
    template_name= "surat/surat-keterangan-penghasilan-tidak-tetap.html"
    surat = get_object_or_404(SuketPenghasilanTidakTetap, id=id)

    # Mengisi template dengan data surat
    context = {
    'nama': surat.nama,
    'umur': surat.umur,
    'pekerjaan': surat.pekerjaan,
    'alamat': surat.alamat,
    'penghasilan': surat.penghasilan,
    'date': surat.date,
}
    
    return render(request,template_name, context)

@login_required
def detail_suketpenghasilantidaktetap(request, id):
    template_name = "backend/detail_suketpenghasilantidaktetap.html"  # Template untuk halaman detail
    
    # Mengambil objek SuketPenghasilanTidakTetap berdasarkan ID
    suket = get_object_or_404(SuketPenghasilanTidakTetap, id=id)
    
    # Mengirim data ke template
    context = {
        'suket': suket,
    }
    
    return render(request, template_name, context)

@login_required
def suketusaha(request):
    template_name = "backend/suketusaha.html"
    
    suket = SuketUsaha.objects.all()
    private = SuketUsaha.objects.filter(penulis=request.user)

    def save_file_with_underscore(file):
        if file:
            new_filename = file.name.replace(" ", "_")  # Mengganti spasi dengan underscore
            return fs.url(fs.save(new_filename, file))
        return None

    if request.method == "POST":
        fs = FileSystemStorage()

        myfile_pengantar = request.FILES.get("pengantarrt")
        myfile_scanktp = request.FILES.get("scanktp")
        myfile_fotousaha = request.FILES.get("fotousaha")
        
        # Jika ada file pengantar RT yang di-upload
        url_pengantar = save_file_with_underscore(myfile_pengantar)
        
        # Jika ada file scan KTP yang di-upload
        url_scanktp = save_file_with_underscore(myfile_scanktp)
        
        # Jika ada file foto usaha yang di-upload
        url_fotousaha = save_file_with_underscore(myfile_fotousaha)
        
        # Membuat objek SuketUsaha baru
        SuketUsaha.objects.create(
            penulis=request.user,
            nama=request.POST.get("inputNama"),
            umur=request.POST.get("inputUmur"),
            pekerjaan=request.POST.get("inputPekerjaan"),
            alamat=request.POST.get("inputAlamat"),
            jenisusaha=request.POST.get("inputJenisUsaha"),
            tahunberdiri=request.POST.get("inputTahunBerdiri"),
            jumlahmodal=request.POST.get("inputJumlahModal"),
            alamatusaha=request.POST.get("inputAlamatUsaha"),
            npnpwp=request.POST.get("inputNpwp"),
            notelepon=request.POST.get("inputNoTelepon"),
            jumlahkaryawan=request.POST.get("inputJumlahKaryawan"),
            keterangan=request.POST.get("inputKeterangan"),
            pengantarrt=url_pengantar,
            scanktp=url_scanktp,
            fotousaha=url_fotousaha,
        )
    
        return redirect('suketusaha')
    
    context = {
        "suket": suket,
        'private': private
    }
    
    return render(request, template_name, context)

@login_required
def edit_suketusaha(request, id):
    template_name = "backend/suketusaha.html"
    
    suket_id = SuketUsaha.objects.get(id=id)

    def save_file_with_underscore(file):
        if file:
            new_filename = file.name.replace(" ", "_")  # Mengganti spasi dengan underscore
            return fs.url(fs.save(new_filename, file))
        return None
    
    if request.method == "POST":
        penulis = request.user
        nama = request.POST.get("inputNama")
        umur = request.POST.get("inputUmur")
        pekerjaan = request.POST.get("inputPekerjaan")
        alamat = request.POST.get("inputAlamat")
        jenisusaha = request.POST.get("inputJenisUsaha")
        tahunberdiri = request.POST.get("inputTahunBerdiri")
        jumlahmodal = request.POST.get("inputJumlahModal")
        alamatusaha = request.POST.get("inputAlamatUsaha")
        npnpwp = request.POST.get("inputNpwp")
        notelepon = request.POST.get("inputNoTelepon")
        jumlahkaryawan = request.POST.get("inputJumlahKaryawan")
        keterangan = request.POST.get("inputKeterangan")

        fs = FileSystemStorage()

        # Mengecek apakah ada file baru yang di-upload
        myfile_pengantar = request.FILES.get("pengantarrt")
        myfile_scanktp = request.FILES.get("scanktp")
        myfile_fotousaha = request.FILES.get("fotousaha")

        # Jika ada file pengantar RT baru yang di-upload
        if myfile_pengantar:
            suket_id.pengantarrt = save_file_with_underscore(myfile_pengantar)
        
        # Jika ada file scan KTP baru yang di-upload
        if myfile_scanktp:
            suket_id.scanktp = save_file_with_underscore(myfile_scanktp)
        
        # Jika ada file foto usaha baru yang di-upload
        if myfile_fotousaha:
            suket_id.fotousaha = save_file_with_underscore(myfile_fotousaha)
        
        # Update data di objek suket_id
        suket_id.penulis = penulis
        suket_id.nama = nama
        suket_id.umur = umur
        suket_id.pekerjaan = pekerjaan
        suket_id.alamat = alamat
        suket_id.jenisusaha = jenisusaha
        suket_id.tahunberdiri = tahunberdiri
        suket_id.jumlahmodal = jumlahmodal
        suket_id.alamatusaha = alamatusaha
        suket_id.npnpwp = npnpwp
        suket_id.notelepon = notelepon
        suket_id.jumlahkaryawan = jumlahkaryawan
        suket_id.keterangan = keterangan
        suket_id.date = timezone.now()
        suket_id.status = 'review'

        suket_id.save()
        
        return redirect('suketusaha')
    
    context = {
        "value": suket_id
    }
    
    return render(request, template_name, context)

@login_required
def setujui_suketusaha(request, id):
    if request.user.is_superuser:
        suket = get_object_or_404(SuketUsaha, id=id)
        suket.status = 'approved'  # Mengubah status menjadi Disetujui
        suket.save()
    return redirect('suketusaha')  # Redirect ke halaman list Suket Usaha

@login_required
def tolak_suketusaha(request, id):
    if request.user.is_superuser:
        suket = get_object_or_404(SuketUsaha, id=id)
        suket.status = 'rejected'  # Mengubah status menjadi Ditolak
        suket.save()
    return redirect('suketusaha')  # Redirect ke halaman list Suket Usaha

@login_required
def delete_suketusaha(request, id):
    SuketUsaha.objects.get(id=id).delete()
    return redirect('suketusaha')

@login_required
def print_suketusaha(request, id):
    # Mengambil data surat
    
    template_name= "surat/surat-keterangan-usaha.html"
    surat = get_object_or_404(SuketUsaha, id=id)

    # Mengisi template dengan data surat
    context = {
    'nama': surat.nama,
    'umur': surat.umur,
    'pekerjaan': surat.pekerjaan,
    'alamat': surat.alamat,
    'jenisusaha': surat.jenisusaha,
    'tahunberdiri': surat.tahunberdiri,
    'jumlahmodal': surat.jumlahmodal,
    'alamatusaha': surat.alamatusaha,
    'npnpwp': surat.npnpwp,
    'notelepon': surat.notelepon,
    'jumlahkaryawan': surat.jumlahkaryawan,
    'keterangan': surat.keterangan,
    'date': surat.date,
}
    
    return render(request,template_name, context)

@login_required
def detail_suketusaha(request, id):
    template_name = "backend/detail_suketusaha.html"  # Template untuk halaman detail
    
    # Mengambil objek SuketUsaha berdasarkan ID
    suket = get_object_or_404(SuketUsaha, id=id)
    
    # Mengirim data ke template
    context = {
        'suket': suket,
    }
    
    return render(request, template_name, context)

@login_required
def suketvaksinnikah(request):
    template_name = "backend/suketvaksinnikah.html"
    
    suket = SuketVaksinNikah.objects.all()
    private = SuketVaksinNikah.objects.filter(penulis=request.user)
    
    if request.method == "POST":
        # Membuat objek SuketVaksinNikah baru
        SuketVaksinNikah.objects.create(
            penulis=request.user,
            nama=request.POST.get("inputNama"),
            jenis_kelamin=request.POST.get("inputjk"),
            ttl=request.POST.get("inputTtl"),
            agama=request.POST.get("inputAgama"),
            pekerjaan=request.POST.get("inputPekerjaan"),
            alamat=request.POST.get("inputAlamat"),
            pengantar=request.POST.get("inputPengantar"),
        )
    
        return redirect('suketvaksinnikah')
    
    context = {
        "suket": suket,
        'private':private
    }
    
    return render(request, template_name, context)

@login_required
def edit_suketvaksinnikah(request, id):
    template_name = "backend/suketvaksinnikah.html"
    
    suket_id = SuketVaksinNikah.objects.get(id=id)
    
    if request.method == "POST":
        # Mengambil input data dari form
        penulis = request.user
        nama = request.POST.get("inputNama")
        jenis_kelamin = request.POST.get("inputjk")
        ttl = request.POST.get("inputTtl")
        agama = request.POST.get("inputAgama")
        pekerjaan = request.POST.get("inputPekerjaan")
        alamat = request.POST.get("inputAlamat")
        pengantar=request.POST.get("inputPengantar")
        
        # Update data di objek suket_id
        suket_id.penulis = penulis
        suket_id.nama = nama
        suket_id.jenis_kelamin = jenis_kelamin
        suket_id.ttl = ttl
        suket_id.agama = agama
        suket_id.pekerjaan = pekerjaan
        suket_id.alamat = alamat
        suket_id.pengantar = pengantar
        suket_id.date = timezone.now()
        suket_id.status='review'

        suket_id.save()
        
        return redirect('suketvaksinnikah')
    
    context = {
        "value": suket_id
    }
    
    return render(request, template_name, context)

@login_required
def setujui_suketvaksinnikah(request, id):
    if request.user.is_superuser:
        suket = get_object_or_404(SuketVaksinNikah, id=id)
        suket.status = 'approved'  # Mengubah status menjadi Disetujui
        suket.save()
    return redirect('suketvaksinnikah')  # Redirect ke halaman list Suket Vaksin Nikah

@login_required
def tolak_suketvaksinnikah(request, id):
    if request.user.is_superuser:
        suket = get_object_or_404(SuketVaksinNikah, id=id)
        suket.status = 'rejected'  # Mengubah status menjadi Ditolak
        suket.save()
    return redirect('suketvaksinnikah')  # Redirect ke halaman list Suket Vaksin Nikah


@login_required
def delete_suketvaksinnikah(request, id):
    SuketVaksinNikah.objects.get(id=id).delete()
    return redirect('suketvaksinnikah')

@login_required
def print_suketvaksinnikah(request, id):
    # Mengambil data surat
    
    template_name= "surat/surat-keterangan-vaksin-nikah.html"
    surat = get_object_or_404(SuketVaksinNikah, id=id)

    # Mengisi template dengan data surat
    context = {
    'nama': surat.nama,
    'jenis_kelamin': surat.jenis_kelamin,
    'ttl': surat.ttl,
    'agama': surat.agama,
    'pekerjaan': surat.pekerjaan,
    'alamat': surat.alamat,
    'pengantar': surat.pengantar,
    'date': surat.date,
}
    
    return render(request,template_name, context)

@login_required
def detail_suketvaksinnikah(request, id):
    template_name = "backend/detail_suketvaksinnikah.html"  # Template untuk halaman detail
    
    # Mengambil objek SuketVaksinNikah berdasarkan ID
    suket = get_object_or_404(SuketVaksinNikah, id=id)
    
    # Mengirim data ke template
    context = {
        'suket': suket,
    }
    
    return render(request, template_name, context)

@login_required
def suketpindahnikah(request):
    template_name = "backend/suketpindahnikah.html"
    
    suket = SuketPindahNikah.objects.all()
    private = SuketPindahNikah.objects.filter(penulis=request.user)
    
    if request.method == "POST":
        # Menyimpan file-file yang di-upload
        fs = FileSystemStorage()

        def save_file(uploaded_file):
            if uploaded_file:
                # Mengganti spasi dengan underscore pada nama file
                filename = uploaded_file.name.replace(" ", "_")
                return fs.save(filename, uploaded_file), fs.url(filename)
            return None, None

        pengantarrt_filename, pengantarrt_url = save_file(request.FILES.get("pengantarrt"))
        scankksuami_filename, scankksuami_url = save_file(request.FILES.get("scankksuami"))
        scankkistri_filename, scankkistri_url = save_file(request.FILES.get("scankkistri"))
        scanktpsuami_filename, scanktpsuami_url = save_file(request.FILES.get("scanktpsuami"))
        scanktpistri_filename, scanktpistri_url = save_file(request.FILES.get("scanktpistri"))
        fotogandeng_filename, fotogandeng_url = save_file(request.FILES.get("fotogandeng"))
        aktaceraikematian_filename, aktaceraikematian_url = save_file(request.FILES.get("aktaceraikematian"))

        # Menyimpan data SuketPindahNikah
        SuketPindahNikah.objects.create(
            penulis=request.user,
            nama1=request.POST.get("inputNama1"),
            ttl1=request.POST.get("inputTtl1"),
            jenis_kelamin1=request.POST.get("inputJenisKelamin1"),
            agama1=request.POST.get("inputAgama1"),
            pekerjaan1=request.POST.get("inputPekerjaan1"),
            alamat1=request.POST.get("inputAlamat1"),
            nama2=request.POST.get("inputNama2"),
            ttl2=request.POST.get("inputTtl2"),
            jenis_kelamin2=request.POST.get("inputJenisKelamin2"),
            agama2=request.POST.get("inputAgama2"),
            pekerjaan2=request.POST.get("inputPekerjaan2"),
            alamat2=request.POST.get("inputAlamat2"),
            pengantarrt=pengantarrt_url,
            scankksuami=scankksuami_url,
            scankkistri=scankkistri_url,
            scanktpsuami=scanktpsuami_url,
            scanktpistri=scanktpistri_url,
            fotogandeng=fotogandeng_url,
            aktaceraikematian=aktaceraikematian_url,
        )
    
        return redirect('suketpindahnikah')
    
    context = {
        "suket": suket,
        'private': private
    }
    
    return render(request, template_name, context)

@login_required
def edit_suketpindahnikah(request, id):
    template_name = "backend/suketpindahnikah.html"
    
    suket_id = SuketPindahNikah.objects.get(id=id)
    
    if request.method == "POST":
        fs = FileSystemStorage()

        def save_file(uploaded_file):
            if uploaded_file:
                # Mengganti spasi dengan underscore pada nama file
                filename = uploaded_file.name.replace(" ", "_")
                return fs.save(filename, uploaded_file), fs.url(filename)
            return None, None

        pengantarrt_filename, pengantarrt_url = save_file(request.FILES.get("pengantarrt"))
        if pengantarrt_url:
            suket_id.pengantarrt = pengantarrt_url

        scankksuami_filename, scankksuami_url = save_file(request.FILES.get("scankksuami"))
        if scankksuami_url:
            suket_id.scankksuami = scankksuami_url

        scankkistri_filename, scankkistri_url = save_file(request.FILES.get("scankkistri"))
        if scankkistri_url:
            suket_id.scankkistri = scankkistri_url

        scanktpsuami_filename, scanktpsuami_url = save_file(request.FILES.get("scanktpsuami"))
        if scanktpsuami_url:
            suket_id.scanktpsuami = scanktpsuami_url

        scanktpistri_filename, scanktpistri_url = save_file(request.FILES.get("scanktpistri"))
        if scanktpistri_url:
            suket_id.scanktpistri = scanktpistri_url

        fotogandeng_filename, fotogandeng_url = save_file(request.FILES.get("fotogandeng"))
        if fotogandeng_url:
            suket_id.fotogandeng = fotogandeng_url

        aktaceraikematian_filename, aktaceraikematian_url = save_file(request.FILES.get("aktaceraikematian"))
        if aktaceraikematian_url:
            suket_id.aktaceraikematian = aktaceraikematian_url

        # Mengupdate data lainnya
        suket_id.penulis = request.user
        suket_id.nama1 = request.POST.get("inputNama1")
        suket_id.ttl1 = request.POST.get("inputTtl1")
        suket_id.jenis_kelamin1 = request.POST.get("inputJenisKelamin1")
        suket_id.agama1 = request.POST.get("inputAgama1")
        suket_id.pekerjaan1 = request.POST.get("inputPekerjaan1")
        suket_id.alamat1 = request.POST.get("inputAlamat1")
        suket_id.nama2 = request.POST.get("inputNama2")
        suket_id.ttl2 = request.POST.get("inputTtl2")
        suket_id.jenis_kelamin2 = request.POST.get("inputJenisKelamin2")
        suket_id.agama2 = request.POST.get("inputAgama2")
        suket_id.pekerjaan2 = request.POST.get("inputPekerjaan2")
        suket_id.alamat2 = request.POST.get("inputAlamat2")
        suket_id.date = timezone.now()
        suket_id.status = 'review'

        suket_id.save()
        
        return redirect('suketpindahnikah')
    
    context = {
        "value": suket_id
    }
    
    return render(request, template_name, context)


@login_required
def setujui_suketpindahnikah(request, id):
    if request.user.is_superuser:
        suket = get_object_or_404(SuketPindahNikah, id=id)
        suket.status = 'approved'  # Mengubah status menjadi Disetujui
        suket.save()
    return redirect('suketpindahnikah')  # Redirect ke halaman list Suket Pindah Nikah

@login_required
def tolak_suketpindahnikah(request, id):
    if request.user.is_superuser:
        suket = get_object_or_404(SuketPindahNikah, id=id)
        suket.status = 'rejected'  # Mengubah status menjadi Ditolak
        suket.save()
    return redirect('suketpindahnikah')  # Redirect ke halaman list Suket Pindah Nikah

@login_required
def delete_suketpindahnikah(request, id):
    SuketPindahNikah.objects.get(id=id).delete()
    return redirect('suketpindahnikah')

@login_required
def print_suketpindahnikah(request, id):
    # Mengambil data surat
    
    template_name= "surat/surat-keterangan-pindah-nikah.html"
    surat = get_object_or_404(SuketPindahNikah, id=id)

    # Mengisi template dengan data surat
    context = {
    'nama1': surat.nama1,
    'ttl1': surat.ttl1,
    'jenis_kelamin1': surat.jenis_kelamin1,
    'agama1': surat.agama1,
    'pekerjaan1': surat.pekerjaan1,
    'alamat1': surat.alamat1,
    'nama2': surat.nama2,
    'ttl2': surat.ttl2,
    'jenis_kelamin2': surat.jenis_kelamin2,
    'agama2': surat.agama2,
    'pekerjaan2': surat.pekerjaan2,
    'alamat2': surat.alamat2,
    'date': surat.date,
}
    
    return render(request,template_name, context)

@login_required
def detail_suketpindahnikah(request, id):
    template_name = "backend/detail_suketpindahnikah.html"  # Template untuk halaman detail
    
    # Mengambil objek SuketPindahNikah berdasarkan ID
    suket = get_object_or_404(SuketPindahNikah, id=id)
    
    # Mengirim data ke template
    context = {
        'suket': suket,
    }
    
    return render(request, template_name, context)

@login_required
def suketrekkeltani(request):
    template_name = "backend/suketrekkeltani.html"
    
    suket = SuketRekKelTani.objects.all()
    private = SuketRekKelTani.objects.filter(penulis=request.user)
    
    if request.method == "POST":
        # Membuat objek SuketRekKelTani baru
        SuketRekKelTani.objects.create(
            penulis=request.user,
            nama=request.POST.get("inputNama"),
            jabatan=request.POST.get("inputJabatan"),
            sekretariat=request.POST.get("inputSekretariat"),
            tempat=request.POST.get("inputTempat"),
            bantuan=request.POST.get("inputBantuan"),
            tujuan=request.POST.get("inputTujuan")
        )
    
        return redirect('suketrekkeltani')
    
    context = {
        "suket": suket,
        'private':private
    }
    
    return render(request, template_name, context)

@login_required
def edit_suketrekkeltani(request, id):
    template_name = "backend/suketrekkeltani.html"
    
    suket_id = SuketRekKelTani.objects.get(id=id)
    
    if request.method == "POST":
        # Mengambil input data dari form
        penulis = request.user
        nama = request.POST.get("inputNama")
        jabatan = request.POST.get("inputJabatan")
        sekretariat = request.POST.get("inputSekretariat")
        tempat = request.POST.get("inputTempat")
        bantuan = request.POST.get("inputBantuan")
        tujuan = request.POST.get("inputTujuan")
        
        # Update data di objek suket_id
        suket_id.penulis = penulis
        suket_id.nama = nama
        suket_id.jabatan = jabatan
        suket_id.sekretariat = sekretariat
        suket_id.tempat = tempat
        suket_id.bantuan = bantuan
        suket_id.tujuan = tujuan
        suket_id.date = timezone.now()
        suket_id.status='review'

        suket_id.save()
        
        return redirect('suketrekkeltani')
    
    context = {
        "value": suket_id
    }
    
    return render(request, template_name, context)

@login_required
def setujui_suketrekeltani(request, id):
    if request.user.is_superuser:
        suket = get_object_or_404(SuketRekKelTani, id=id)
        suket.status = 'approved'  # Mengubah status menjadi Disetujui
        suket.save()
    return redirect('suketrekkeltani')  # Redirect ke halaman list Suket Rek Kel Tani

@login_required
def tolak_suketrekeltani(request, id):
    if request.user.is_superuser:
        suket = get_object_or_404(SuketRekKelTani, id=id)
        suket.status = 'rejected'  # Mengubah status menjadi Ditolak
        suket.save()
    return redirect('suketrekkeltani')  # Redirect ke halaman list Suket Rek Kel Tani

@login_required
def delete_suketrekkeltani(request, id):
    SuketRekKelTani.objects.get(id=id).delete()
    return redirect('suketrekkeltani')

@login_required
def print_suketrekkeltani(request, id):
    # Mengambil data surat
    
    template_name= "surat/surat-rekomendasi-kelompok-tani.html"
    surat = get_object_or_404(SuketRekKelTani, id=id)

    # Mengisi template dengan data surat
    context = {
    'nama': surat.nama,
    'jabatan': surat.jabatan,
    'sekretariat': surat.sekretariat,
    'tempat': surat.tempat,
    'bantuan': surat.bantuan,
    'tujuan': surat.tujuan,
    'date': surat.date,
}
    
    return render(request,template_name, context)

@login_required
def detail_suketrekkeltani(request, id):
    template_name = "backend/detail_suketrekkeltani.html"  # Template untuk halaman detail
    
    # Mengambil objek SuketRekKelTani berdasarkan ID
    suket = get_object_or_404(SuketRekKelTani, id=id)
    
    # Mengirim data ke template
    context = {
        'suket': suket,
    }
    
    return render(request, template_name, context)

@login_required
def pengumuman(request):
    template_name = "backend/pengumuman.html"
    
    annc = Pengumuman.objects.all()
    
    if request.method == 'POST':
        judul = request.POST.get("inputJudul")
        konten = request.POST.get("inputKonten")
        picture = request.FILES.get("inputGambar")
        
        fs = FileSystemStorage()

        def save_file(uploaded_file):
            if uploaded_file:
                # Mengganti spasi dengan underscore pada nama file
                filename = uploaded_file.name.replace(" ", "_")
                return fs.save(filename, uploaded_file), fs.url(filename)
            return None, None

        # Jika ada file gambar yang di-upload
        picture_filename, url_pengantar = save_file(picture)

        Pengumuman.objects.create(
            penulis=request.user,
            judul=judul,
            konten=konten,
            picture=url_pengantar
        )
        
        return redirect('pengumuman')
        
    context = {
        "annc": annc
    }
    
    return render(request, template_name, context)

@login_required
def edit_pengumuman(request, id):
    template_name = "backend/pengumuman.html"
    
    pengumuman_id = Pengumuman.objects.get(id=id)
    
    if request.method == "POST":
        # Mengambil input data dari form
        judul = request.POST.get("inputJudul")
        konten = request.POST.get("inputKonten")
        picture = request.FILES.get("inputGambar")
        
        fs = FileSystemStorage()

        def save_file(uploaded_file):
            if uploaded_file:
                # Mengganti spasi dengan underscore pada nama file
                filename = uploaded_file.name.replace(" ", "_")
                return fs.save(filename, uploaded_file), fs.url(filename)
            return None, None

        # Jika ada file gambar baru yang di-upload
        if picture:
            picture_filename, url_pengantar = save_file(picture)
            pengumuman_id.picture = url_pengantar
        
        # Update data di objek pengumuman
        pengumuman_id.judul = judul
        pengumuman_id.konten = konten
        pengumuman_id.date = timezone.now()

        pengumuman_id.save()
        
        return redirect('pengumuman')  # Redirect ke halaman pengumuman (sesuaikan dengan rute yang kamu inginkan)
    
    context = {
        "value": pengumuman_id
    }
    
    return render(request, template_name, context)

@login_required
def delete_pengumuman(request, id):
    Pengumuman.objects.get(id=id).delete()
    return redirect('pengumuman')  # Redirect ke halaman pengumuman (sesuaikan dengan rute yang kamu inginkan)

@login_required    
def blog(request):
    template_name = "backend/blog.html"
    
    blg = Blog.objects.all()
    
    if request.method == 'POST':
        judul = request.POST.get("inputJudul")
        konten = request.POST.get("inputKonten")
        picture = request.FILES.get("inputGambar")
        
        fs = FileSystemStorage()

        def save_file(uploaded_file):
            if uploaded_file:
                # Mengganti spasi dengan underscore pada nama file
                filename = uploaded_file.name.replace(" ", "_")
                return fs.save(filename, uploaded_file), fs.url(filename)
            return None, None

        # Jika ada file gambar yang di-upload
        picture_filename, url_pengantar = save_file(picture)

        Blog.objects.create(
            penulis=request.user,
            judul=judul,
            konten=konten,
            picture=url_pengantar
        )
        
        return redirect('blog')
        
    context = {
        "blg": blg,
        "title": "Halaman Berita"
    }
    
    return render(request, template_name, context)

@login_required
def edit_blog(request, id):
    template_name = "backend/blog.html"
    
    blog_id = Blog.objects.get(id=id)
    
    if request.method == "POST":
        # Mengambil input data dari form
        judul = request.POST.get("inputJudul")
        konten = request.POST.get("inputKonten")
        picture = request.FILES.get("inputGambar")
        
        fs = FileSystemStorage()

        def save_file(uploaded_file):
            if uploaded_file:
                # Mengganti spasi dengan underscore pada nama file
                filename = uploaded_file.name.replace(" ", "_")
                return fs.save(filename, uploaded_file), fs.url(filename)
            return None, None

        # Jika ada file gambar baru yang di-upload
        if picture:
            picture_filename, url_pengantar = save_file(picture)
            blog_id.picture = url_pengantar
        
        # Update data di objek blog
        blog_id.judul = judul
        blog_id.konten = konten
        blog_id.date = timezone.now()

        blog_id.save()
        
        return redirect('blog')  # Redirect ke halaman blog (sesuaikan dengan rute yang kamu inginkan)
    
    context = {
        "value": blog_id
    }
    
    return render(request, template_name, context)

@login_required
def delete_blog(request, id):
    Blog.objects.get(id=id).delete()
    return redirect('blog')  # Redirect ke halaman pengumuman (sesuaikan dengan rute yang kamu inginkan)

@login_required
def detail_blog(request, id):
    template_name = "backend/detailblog.html"
    
    blg = Blog.objects.get(id=id)
    
    context = {
        "blg" : blg
    }
    
    return render (request, template_name, context)

@login_required
def logoutPage(request):
    logout(request)
    return redirect('welcome')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        nik = request.POST['nik']
        ktp = request.FILES['ktp']

        # Validasi password
        if password != password2:
            return render(request, 'backend/register.html', {'error': 'Passwords do not match'})
        
        # Validasi apakah NIK sudah ada di database
        if Profile.objects.filter(nik=nik).exists():
            return render(request, 'backend/register.html', {'error': 'NIK already exists'})

        # Validasi apakah username sudah ada di database
        if User.objects.filter(username=username).exists():
            return render(request, 'backend/register.html', {'error': 'Username already exists'})
        
        # Buat user baru
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

        # Menyimpan KTP dengan mengganti spasi dengan underscore
        fs = FileSystemStorage()
        ktp_filename = ktp.name.replace(" ", "_")  # Mengganti spasi dengan underscore
        filename = fs.save(ktp_filename, ktp)
        ktp_url = fs.url(filename)

        # Update profil pengguna dengan NIK dan KTP
        user.profile.nik = nik
        user.profile.ktp = ktp_url
        user.profile.save()

        # Login otomatis setelah registrasi
        login(request, user)

        return redirect('dashboard')  # Redirect ke halaman utama setelah registrasi

    return render(request, 'backend/register.html')

@login_required
def profile(request):
    template_name = "backend/profile.html"
     # Ambil user yang sedang login
    user = request.user

    # Ambil profil terkait user
    profile = Profile.objects.get(user=user)
    
    context = {
        "user":user,
        "profile" : profile,
    }
    
    
    return render(request,template_name, context)

@login_required
def daftaruser(request):
    template_name = "backend/daftaruser.html"
   
    profile = Profile.objects.all()
    
    context = {
        "profile":profile,
     
    }
    return render(request,template_name, context)

@login_required
def detailuser(request,id):
    template_name = "backend/detailuser.html"
   
    user = get_object_or_404(User, id=id)
    profile = user.profile
    
    context = {
        "profile":profile,
     
    }
    
    return render(request,template_name, context)

@login_required
def hapususers(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect(daftaruser)

@login_required
def edituser(request, id):
    # Mengambil objek user dan profil berdasarkan ID
    user = get_object_or_404(User, id=id)
    profile = user.profile

    if request.method == 'POST':
        # Mengambil data dari form
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        nik = request.POST['nik']

        # Mengambil file KTP yang diupload (jika ada)
        if 'ktp' in request.FILES:
            ktp = request.FILES['ktp']
            # Ganti spasi dengan underscore pada nama file
            ktp.name = ktp.name.replace(' ', '_')
            fs = FileSystemStorage()
            filename = fs.save(ktp.name, ktp)
            ktp_url = fs.url(filename)
            profile.ktp = ktp_url  # Update KTP jika ada

        # Update data user
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        # Update data profil
        profile.nik = nik
        profile.save()

        # Redirect setelah penyimpanan
        return redirect('daftar_user')  # Redirect ke halaman detail user setelah update

    # Jika requestnya GET, tampilkan form dengan data user yang sudah ada
    context = {
        'user': user,
        'profile': profile,
    }
    return render(request, 'backend/edituser.html', context)

@login_required
def datapengaduanasing(request):
    template_name = "backend/pengaduanasing.html"
   
    aduan = PengaduanAsing.objects.all()
    
    context = {
        "aduans":aduan,
     
    }
    return render(request,template_name, context)

@login_required
def detailpengaduanasing(request,id):
    template_name = "backend/detailpengaduanasing.html"
   
    aduan = PengaduanAsing.objects.get(id=id)
    
    context = {
        "aduans":aduan,
     
    }
    return render(request,template_name, context)

@login_required
def deletepengaduanasing(request,id):
    datas = PengaduanAsing.objects.get(id=id)
    datas.delete()
    return redirect(datapengaduanasing)

@login_required
def register_super_admin(request):
    if request.method == 'POST':
        # Ambil data dari form POST
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Validasi password cocok
        if password1 != password2:
            return render(request, 'backend/register_super_admin.html', {
                'error': 'Passwords do not match'
            })

        # Cek apakah username sudah ada
        if User.objects.filter(username=username).exists():
            return render(request, 'backend/register_super_admin.html', {
                'error': 'Username already exists'
            })

        # Membuat super admin baru
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.first_name = first_name
        user.last_name = last_name
        user.is_superuser = True  # Beri hak akses superuser
        user.is_staff = True  # Beri akses admin dashboard
        user.save()

        return redirect('dashboard')  # Redirect setelah registrasi berhasil

    return render(request, 'backend/register_super_admin.html')