from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from dashboard.models import *
from django.core.files.storage import FileSystemStorage
import requests
from django.core.mail import send_mail

def welcome(request):
    template_name = "frontend/homepage.html"
    annc = Pengumuman.objects.all().order_by('-id')[:4]
    
    if request.method == 'POST':
        # Ambil data dari POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        ktp_file = request.FILES.get("ktp")
        fs = FileSystemStorage()
        if ktp_file:
            ktp_filename = fs.save(ktp_file.name, ktp_file)
            ktp_url = fs.url(ktp_filename)
        else:
            ktp_url = None
        
        PengaduanAsing.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message,
            ktp=ktp_url
        )

        # Buat subjek dan isi email
        subject = f'Pengaduan dari {name}'
        # Buat body HTML email
        html_message = f'''
        <div style="font-family: Arial, sans-serif; padding: 20px; border: 1px solid #ddd; border-radius: 5px; max-width: 600px; margin: 0 auto; background-color: #f9f9f9;">
            <h1 style="color: #4CAF50; text-align: center;">Pengaduan Baru</h1>
            <hr style="border: 1px solid #ddd;">
            <p><strong>Nama:</strong> {name}</p>
            <p><strong>Email:</strong> <a href="mailto:{email}" style="color: #4CAF50;">{email}</a></p>
            <p><strong>Telepon:</strong> <a href="tel:{phone}" style="color: #4CAF50;">{phone}</a></p>
            <p><strong>Pesan:</strong></p>
            <div style="padding: 10px; background-color: #fff; border: 1px solid #ddd; border-radius: 5px;">
              {message}
            </div>
            <hr style="border: 1px solid #ddd;">
            <p style="text-align: center; font-size: 12px; color: #888;">Email ini dikirimkan secara otomatis dari sistem pengaduan masyarakat desa Kerta Buana.</p>
        </div>
        '''

        # Kirim email menggunakan send_mail
        send_mail(
            subject,
            '',  # Body plaintext (biarkan kosong jika tidak perlu)
            email,  # Dari siapa (pengirim)
            ['desakertabuana24@gmail.com'],  # Kepada siapa email dikirim
            fail_silently=False,
            html_message=html_message  # Pesan HTML
        )

        # Setelah email dikirim, redirect atau tampilkan pesan sukses
        return render(request, 'frontend/sendberhasil.html')
    
    context = {
        "annc" : annc
    }
    
    return render (request, template_name, context)


def detail_pengumuman(request, id):
    template_name = "frontend/detailpengumuman.html"
    
    annc = Pengumuman.objects.get(id=id)
    
    context = {
        "annc" : annc
    }
    
    return render (request, template_name, context)


def blog(request):
    template_name = "frontend/blog.html"
    
    blg = Blog.objects.all().order_by('-date')
    paginator = Paginator(blg, 6)  # 6 posts per page
    page_number = request.GET.get('page')
    blog_posts = paginator.get_page(page_number)
    
    context = {
        "blg" : blg,
        'blog_posts': blog_posts
    }
    
    return render (request, template_name, context)


def detail_blog(request, id):
    template_name = "frontend/detailblog.html"
    
    blg = Blog.objects.get(id=id)
    
    context = {
        "blg" : blg
    }
    
    return render (request, template_name, context)


def loginPage(request):
    
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    template_name = "frontend/login.html"
    
    if request.method == "POST":
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
      
        if user is not None:
             # Cek apakah user sudah punya profil, jika belum, buat profil
            if not hasattr(user, 'profile'):
                Profile.objects.create(user=user)
                
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('welcome')
            print("login gagal")
    
    return render(request, template_name)

