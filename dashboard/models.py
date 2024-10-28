from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class SuketPermohonanKTP(models.Model):
    STATUS_CHOICES = [
        ('review', 'Proses Review'),
        ('approved', 'Disetujui'),
        ('rejected', 'Ditolak'),
    ]


    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=255)
    nokk = models.CharField(max_length=255)
    nik = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    pengantarrt = models.URLField(blank=True, null=True)
    scankk = models.URLField(blank=True, null=True)
    scanijasahakta = models.URLField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='review')
    
    def __str__(self):
        return "{} - {}".format(self.penulis, self.nik)
class SuketBelumMenikah(models.Model):
    STATUS_CHOICES = [
        ('review', 'Proses Review'),
        ('approved', 'Disetujui'),
        ('rejected', 'Ditolak'),
    ]


    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=255)
    jenis_kelamin = models.CharField(max_length=255)
    ttl = models.CharField(max_length=255)
    suku = models.CharField(max_length=255)
    agama = models.CharField(max_length=255)
    nik = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    persyaratan = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='review')
    
    def __str__(self):
        return "{} - {}".format(self.penulis, self.nik)

class SuketTidakMampu(models.Model):
    STATUS_CHOICES = [
        ('review', 'Proses Review'),
        ('approved', 'Disetujui'),
        ('rejected', 'Ditolak'),
    ]


    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=255)
    jenis_kelamin = models.CharField(max_length=255)
    ttl = models.CharField(max_length=255)
    suku = models.CharField(max_length=255)
    agama = models.CharField(max_length=255)
    nik = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    pekerjaan = models.CharField(max_length=255)
    dusun = models.CharField(max_length=255, blank=True, null=True)
    keperluan = models.CharField(max_length=255, blank=True, null=True)
    scankk = models.URLField(blank=True, null=True)
    pengantarrt = models.URLField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='review')
    
    def __str__(self):
        return "{} - {}".format(self.penulis, self.nik)

class SKCK(models.Model):
    STATUS_CHOICES = [
        ('review', 'Proses Review'),
        ('approved', 'Disetujui'),
        ('rejected', 'Ditolak'),
    ]


    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=255)
    jenis_kelamin = models.CharField(max_length=255)
    ttl = models.CharField(max_length=255)
    suku = models.CharField(max_length=255)
    agama = models.CharField(max_length=255)
    nik = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    pekerjaan = models.CharField(max_length=255)
    kawin = models.CharField(max_length=255)
    pendidikanterakhir = models.CharField(max_length=255)
    persyaratan = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='review')
    scanktp = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return "{} - {}".format(self.penulis, self.nik)
    
class SuketKTPBedaNama(models.Model):
    STATUS_CHOICES = [
        ('review', 'Proses Review'),
        ('approved', 'Disetujui'),
        ('rejected', 'Ditolak'),
    ]


    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=255)
    jenis_kelamin = models.CharField(max_length=255)
    ttl = models.CharField(max_length=255)
    agama = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    pekerjaan = models.CharField(max_length=255)
    namadokumen1=models.CharField(max_length=255, blank=True, null=True)
    dokumen1=models.CharField(max_length=255, blank=True, null=True)
    namadokumen2=models.CharField(max_length=255, blank=True, null=True)
    dokumen2=models.CharField(max_length=255, blank=True, null=True)
    berkas1 = models.URLField(blank=True, null=True)
    berkas2 = models.URLField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='review')
    
    def __str__(self):
        return "{}".format(self.penulis)
    
class SuketAhliWaris(models.Model):
    STATUS_CHOICES = [
        ('review', 'Proses Review'),
        ('approved', 'Disetujui'),
        ('rejected', 'Ditolak'),
    ]


    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    almarhum =models.CharField(max_length=255, blank=True, null=True)
    suami =models.CharField(max_length=255, blank=True, null=True)
    istri =models.CharField(max_length=255, blank=True, null=True)
    jumlahanak =models.CharField(max_length=255, blank=True, null=True)
    tanggalmeninggal =models.CharField(max_length=255, blank=True, null=True)
    bulanmeninggal =models.CharField(max_length=255, blank=True, null=True)
    tahunmeninggal =models.CharField(max_length=255, blank=True, null=True)
    nama1 = models.CharField(max_length=255)
    ttl1 = models.CharField(max_length=255)
    alamat1 = models.CharField(max_length=255)
    nama2 = models.CharField(max_length=255)
    ttl2 = models.CharField(max_length=255)
    alamat2 = models.CharField(max_length=255)
    nama3 = models.CharField(max_length=255)
    ttl3 = models.CharField(max_length=255)
    alamat3 = models.CharField(max_length=255)
    nama4 = models.CharField(max_length=255)
    ttl4 = models.CharField(max_length=255)
    alamat4 = models.CharField(max_length=255)
    skkematian = models.URLField(blank=True, null=True)
    scanktpkkahliwaris1 = models.URLField(blank=True, null=True)
    scanktpkkahliwaris2 = models.URLField(blank=True, null=True)
    scanktpkkahliwaris3 = models.URLField(blank=True, null=True)
    scanktpkkahliwaris4 = models.URLField(blank=True, null=True)
    scanktpsaksi1 = models.URLField(blank=True, null=True)
    scanktpsaksi2 = models.URLField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='review')
    
    def __str__(self):
        return "{} ".format(self.penulis)
    
class SuketMTQ(models.Model):
    STATUS_CHOICES = [
        ('review', 'Proses Review'),
        ('approved', 'Disetujui'),
        ('rejected', 'Ditolak'),
    ]


    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=255)
    jenis_kelamin = models.CharField(max_length=255)
    ttl = models.CharField(max_length=255)
    suku = models.CharField(max_length=255)
    agama = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    pekerjaan = models.CharField(max_length=255)
    dusun = models.CharField(max_length=255,blank=True, null=True)
    tahunmenetap = models.CharField(max_length=255,blank=True, null=True)
    keperluan = models.CharField(max_length=255,blank=True, null=True)
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='review')
    
    def __str__(self):
        return "{} ".format(self.penulis)
    
class SuketKehilangan(models.Model):
    STATUS_CHOICES = [
        ('review', 'Proses Review'),
        ('approved', 'Disetujui'),
        ('rejected', 'Ditolak'),
    ]


    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=255)
    jenis_kelamin = models.CharField(max_length=255)
    umur = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    pekerjaan = models.CharField(max_length=255)
    harikehilangan = models.CharField(max_length=255,blank=True, null=True)
    barang1 = models.CharField(max_length=255)
    barang2 = models.CharField(max_length=255)
    barang3 = models.CharField(max_length=255)
    tempat1 = models.CharField(max_length=255)
    tempat2 = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='review')
    
    def __str__(self):
        return "{} ".format(self.penulis)
    
class SuketKelahiran(models.Model):
    STATUS_CHOICES = [
        ('review', 'Proses Review'),
        ('approved', 'Disetujui'),
        ('rejected', 'Ditolak'),
    ]


    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    namab = models.CharField(max_length=255)
    jenis_kelaminb = models.CharField(max_length=255)
    tanggal_lahirb = models.CharField(max_length=255)
    tempat_lahirb = models.CharField(max_length=255)
    agamab = models.CharField(max_length=255)
    alamatb = models.CharField(max_length=255)
    anakke = models.CharField(max_length=255)
    namaa = models.CharField(max_length=255)
    umura = models.CharField(max_length=255)
    pekerjaana = models.CharField(max_length=255)
    alamata = models.CharField(max_length=255)
    namai = models.CharField(max_length=255)
    umuri = models.CharField(max_length=255)
    pekerjaani = models.CharField(max_length=255)
    alamati = models.CharField(max_length=255)
    persyaratan = models.CharField(max_length=255,blank=True, null=True)
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='review')
    kkb = models.URLField(blank=True, null=True)
    scanfcbnb = models.URLField(blank=True, null=True)
    scanfcktportub = models.URLField(blank=True, null=True)
    scanfcktpsaksib1 = models.URLField(blank=True, null=True)
    scanfcktpsaksib2 = models.URLField(blank=True, null=True)
    kkd = models.URLField(blank=True, null=True)
    kk_ktportud = models.URLField(blank=True, null=True)
    scanfcktpsaksid1 = models.URLField(blank=True, null=True)
    scanfcktpsaksid2 = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return "{} ".format(self.penulis)
    
class SuketKematian(models.Model):
    STATUS_CHOICES = [
        ('review', 'Proses Review'),
        ('approved', 'Disetujui'),
        ('rejected', 'Ditolak'),
    ]


    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=255)
    nip = models.CharField(max_length=255)
    jabatan = models.CharField(max_length=255)
    nokk = models.CharField(max_length=255)
    namaalm = models.CharField(max_length=255)
    nikalm = models.CharField(max_length=255)
    ttlalm = models.CharField(max_length=255)
    agamaalm = models.CharField(max_length=255)
    anakkealm = models.CharField(max_length=255)
    ibualm = models.CharField(max_length=255)
    ayahalm = models.CharField(max_length=255)
    pekerjaanalm = models.CharField(max_length=255)
    kewarganegaraanalm = models.CharField(max_length=255)
    alamatalm = models.CharField(max_length=255)
    tanggal_kematian = models.CharField(max_length=255)
    jam_kematian = models.CharField(max_length=255)
    tempat_kematian = models.CharField(max_length=255)
    penyebab_kematian = models.CharField(max_length=255)
    tmptmakam = models.CharField(max_length=255)
    tanggal_pmkn = models.CharField(max_length=255)
    jam_pmkn = models.CharField(max_length=255)
    pengantarrt = models.URLField(blank=True, null=True)
    scankk = models.URLField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='review')
    
    def __str__(self):
        return "{} ".format(self.nama)
    
class SuketPenghasilanTidakTetap(models.Model):
    STATUS_CHOICES = [
        ('review', 'Proses Review'),
        ('approved', 'Disetujui'),
        ('rejected', 'Ditolak'),
    ]


    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=255)
    umur = models.CharField(max_length=255)
    pekerjaan = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    penghasilan = models.CharField(max_length=255,blank=True, null=True)
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='review')
    pengantarrt = models.URLField(blank=True, null=True)
    scankk = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return "{} ".format(self.penulis)
    
class SuketUsaha(models.Model):
    STATUS_CHOICES = [
        ('review', 'Proses Review'),
        ('approved', 'Disetujui'),
        ('rejected', 'Ditolak'),
    ]


    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=255)
    umur = models.CharField(max_length=255)
    pekerjaan = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    jenisusaha = models.CharField(max_length=255)
    tahunberdiri = models.CharField(max_length=255)
    jumlahmodal = models.CharField(max_length=255)
    alamatusaha = models.CharField(max_length=255)
    npnpwp = models.CharField(max_length=255)
    notelepon = models.CharField(max_length=255)
    jumlahkaryawan = models.CharField(max_length=255)
    keterangan = models.TextField()
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='review')
    pengantarrt = models.URLField(blank=True, null=True)
    scanktp = models.URLField(blank=True, null=True)
    fotousaha = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return "{} ".format(self.penulis)
    
class SuketVaksinNikah(models.Model):
    STATUS_CHOICES = [
        ('review', 'Proses Review'),
        ('approved', 'Disetujui'),
        ('rejected', 'Ditolak'),
    ]


    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=255)
    jenis_kelamin = models.CharField(max_length=255)
    ttl = models.CharField(max_length=255)
    agama = models.CharField(max_length=255)
    pekerjaan = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    pengantar = models.CharField(max_length=255,blank=True, null=True)
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='review')
    
    def __str__(self):
        return "{} ".format(self.penulis)

class SuketPindahNikah(models.Model):
    STATUS_CHOICES = [
        ('review', 'Proses Review'),
        ('approved', 'Disetujui'),
        ('rejected', 'Ditolak'),
    ]


    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nama1 = models.CharField(max_length=255)
    ttl1 = models.CharField(max_length=255)
    jenis_kelamin1 = models.CharField(max_length=255)
    agama1 = models.CharField(max_length=255)
    pekerjaan1 = models.CharField(max_length=255)
    alamat1 = models.CharField(max_length=255)
    nama2 = models.CharField(max_length=255)
    ttl2 = models.CharField(max_length=255)
    jenis_kelamin2 = models.CharField(max_length=255)
    agama2 = models.CharField(max_length=255)
    pekerjaan2 = models.CharField(max_length=255)
    alamat2 = models.CharField(max_length=255)
    pengantarrt = models.URLField(blank=True, null=True)
    scankksuami = models.URLField(blank=True, null=True)
    scankkistri = models.URLField(blank=True, null=True)
    scanktpsuami = models.URLField(blank=True, null=True)
    scanktpistri = models.URLField(blank=True, null=True)
    fotogandeng = models.URLField(blank=True, null=True)
    aktaceraikematian = models.URLField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='review')
    
    def __str__(self):
        return "{} ".format(self.penulis)

class SuketRekKelTani(models.Model):
    STATUS_CHOICES = [
        ('review', 'Proses Review'),
        ('approved', 'Disetujui'),
        ('rejected', 'Ditolak'),
    ]


    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=255)
    jabatan = models.CharField(max_length=255)
    sekretariat = models.CharField(max_length=255)
    tempat = models.CharField(max_length=255)
    bantuan = models.CharField(max_length=255)
    tujuan = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='review')
    
    def __str__(self):
        return "{} ".format(self.penulis)
    
class Pengumuman(models.Model):
    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    judul = models.CharField(max_length=200) 
    konten = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    picture = models.URLField(blank=True, null=True)
    
    def __str__(self):
      return "{} - {}".format(self.judul, self.konten)
class Blog(models.Model):
    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    judul = models.CharField(max_length=200) 
    konten = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    picture = models.URLField(blank=True, null=True)
    
    def __str__(self):
      return "{} - {}".format(self.judul, self.konten)
  
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nik = models.CharField(max_length=200)
    ktp = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class PengaduanAsing(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    ktp = models.URLField(blank=True, null=True)
    
    def __str__(self):
      return "{} - {}".format(self.name, self.email)