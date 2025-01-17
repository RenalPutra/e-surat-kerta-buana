from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",dashboard, name="dashboard"),
    path("suket-permohonan-ktp/", suketpermohonanktp, name="suketpermohonanktp"),
    path("suket-permohonan-ktp/edit/<int:id>", edit_suketpermohonanktp, name="edit_suketpermohonanktp"),
    path('suket-permohonan-ktp/setujui/<int:id>/', setujui_suketpermohonanktp, name='setujui_suketpermohonanktp'),
    path('suket-permohonan-ktp/tolak/<int:id>/', tolak_suketpermohonanktp, name='tolak_suketpermohonanktp'),
    path("suket-permohonan-ktp/delete/<int:id>", delete_suketpermohonanktp, name="delete_suketpermohonanktp"),
    path("suket-permohonan-ktp/print/<int:id>", print_suketpermohonanktp, name="print_suketpermohonanktp"),
    path("suket-permohonan-ktp/detail/<int:id>", detail_suketpermohonanktp, name="detail_suketpermohonanktp"),
    path("suket-belum-menikah/",suketbelummenikah,  name="suketbelummenikah"),
    path("suket-belum-menikah/edit/<int:id>",edit_suketbelummenikah,  name="edit_suketbelummenikah"),
    path('suket-belum-menikah/setujui/<int:id>/', setujui_suketbelummenikah, name='setujui_suketbelummenikah'),
    path('suket-belum-menikah/tolak/<int:id>/', tolak_suketbelummenikah, name='tolak_suketbelummenikah'),
    path("suket-belum-menikah/delete/<int:id>",delete_suketbelummenikah,  name="delete_suketbelummenikah"),
    path('suket-belum-menikah/print/<int:id>/', print_suketbelummenikah, name='print_suketbelummenikah'),
    path("suket-belum-menikah/detail/<int:id>", detail_suketbelummenikah, name="detail_suketbelummenikah"),
    path("suket-tidak-mampu/",sukettidakmampu,  name="sukettidakmampu"),
    path("suket-tidak-mampu/edit/<int:id>",edit_sukettidakmampu,  name="edit_sukettidakmampu"),
    path('suket-tidak-mampu/setujui/<int:id>/', setujui_sukettidakmampu, name='setujui_sukettidakmampu'),
    path('suket-tidak-mampu/tolak/<int:id>/', tolak_sukettidakmampu, name='tolak_sukettidakmampu'),
    path("suket-tidak-mampu/delete/<int:id>",delete_sukettidakmampu,  name="delete_sukettidakmampu"),
    path("suket-tidak-mampu/print/<int:id>",print_sukettidakmampu,  name="print_sukettidakmampu"),
    path("suket-tidak-mampu/detail/<int:id>", detail_sukettidakmampu, name="detail_sukettidakmampu"),
    path("skck/",skck,  name="skck"),
    path("skck/edit/<int:id>",edit_skck,  name="edit_skck"),
    path('skck/setujui/<int:id>/', setujui_skck, name='setujui_skck'),
    path('skck/tolak/<int:id>/', tolak_skck, name='tolak_skck'),
    path("skck/delete/<int:id>",delete_skck,  name="delete_skck"),
    path("skck/print/<int:id>",print_skck,  name="print_skck"),
    path("skck/detail/<int:id>", detail_skck, name="detail_skck"),
    path("suket-ktp-beda-nama/",suketktpbedanama,  name="suketktpbedanama"),
    path("suket-ktp-beda-nama/edit/<int:id>",edit_suketktpbedanama,  name="edit_suketktpbedanama"),
    path('suket-ktp-beda-nama/setujui/<int:id>/', setujui_suketktpbedanama, name='setujui_suketktpbedanama'),
    path('suket-ktp-beda-nama/tolak/<int:id>/', tolak_suketktpbedanama, name='tolak_suketktpbedanama'),
    path("suket-ktp-beda-nama/delete/<int:id>",delete_suketktpbedanama,  name="delete_suketktpbedanama"),
    path("suket-ktp-beda-nama/print/<int:id>",print_suketktpbedanama,  name="print_suketktpbedanama"),
    path("suket-ktp-beda-nama/detail/<int:id>", detail_suketktpbedanama, name="detail_suketktpbedanama"),
    path("suket-ahli-waris/",suketahliwaris,  name="suketahliwaris"),
    path("suket-ahli-waris/edit/<int:id>",edit_suketahliwaris,  name="edit_suketahliwaris"),
    path('suket-ahli-waris/setujui/<int:id>/', setujui_suketahliwaris, name='setujui_suketahliwaris'),
    path('suket-ahli-waris/tolak/<int:id>/', tolak_suketahliwaris, name='tolak_suketahliwaris'),
    path("suket-ahli-waris/delete/<int:id>",delete_suketahliwaris,  name="delete_suketahliwaris"),
    path("suket-ahli-waris/print/<int:id>",print_suketahliwaris,  name="print_suketahliwaris"),
    path("suket-ahli-waris/detail/<int:id>", detail_suketahliwaris, name="detail_suketahliwaris"),
    path("suket-MTQ/",suketMTQ,  name="suketMTQ"),
    path("suket-MTQ/edit/<int:id>",edit_suketMTQ,  name="edit_suketMTQ"),
    path('suket-mtq/setujui/<int:id>/', setujui_suketmtq, name='setujui_suketmtq'),
    path('suket-mtq/tolak/<int:id>/', tolak_suketmtq, name='tolak_suketmtq'),
    path("suket-MTQ/delete/<int:id>",delete_suketMTQ,  name="delete_suketMTQ"),
    path("suket-MTQ/print/<int:id>",print_suketMTQ,  name="print_suketMTQ"),
    path("suket-mtq/detail/<int:id>", detail_suketmtq, name="detail_suketmtq"),
    path("suket-kehilangan/",suketkehilangan,  name="suketkehilangan"),
    path("suket-kehilangan/edit/<int:id>",edit_suketkehilangan,  name="edit_suketkehilangan"),
    path('suket-kehilangan/setujui/<int:id>/', setujui_suketkehilangan, name='setujui_suketkehilangan'),
    path('suket-kehilangan/tolak/<int:id>/', tolak_suketkehilangan, name='tolak_suketkehilangan'),
    path("suket-kehilangan/delete/<int:id>",delete_suketkehilangan,  name="delete_suketkehilangan"),
    path("suket-kehilangan/print/<int:id>",print_suketkehilangan,  name="print_suketkehilangan"),
    path("suket-kehilangan/detail/<int:id>", detail_suketkehilangan, name="detail_suketkehilangan"),
    path("suket-kelahiran/",suketkelahiran,  name="suketkelahiran"),
    path("suket-kelahiran/edit/<int:id>",edit_suketkelahiran,  name="edit_suketkelahiran"),
    path('suket-kelahiran/setujui/<int:id>/', setujui_suketkelahiran, name='setujui_suketkelahiran'),
    path('suket-kelahiran/tolak/<int:id>/', tolak_suketkelahiran, name='tolak_suketkelahiran'),
    path("suket-kelahiran/delete/<int:id>",delete_suketkelahiran,  name="delete_suketkelahiran"),
    path("suket-kelahiran/print/<int:id>",print_suketkelahiran,  name="print_suketkelahiran"),
    path("suket-kelahiran/detail/<int:id>", detail_suketkelahiran, name="detail_suketkelahiran"),
    path("suket-kematian/",suketkematian,  name="suketkematian"),
    path("suket-kematian/edit/<int:id>",edit_suketkematian,  name="edit_suketkematian"),
    path('suket-kematian/setujui/<int:id>/', setujui_suketkematian, name='setujui_suketkematian'),
    path('suket-kematian/tolak/<int:id>/', tolak_suketkematian, name='tolak_suketkematian'),
    path("suket-kematian/delete/<int:id>",delete_suketkematian,  name="delete_suketkematian"),
    path("suket-kematian/print/<int:id>",print_suketkematian,  name="print_suketkematian"),
    path("suket-kematian/detail/<int:id>", detail_suketkematian, name="detail_suketkematian"),
    path("suket-penghasilan-tidak-tetap/",suketpenghasilantidaktetap,  name="suketpenghasilantidaktetap"),
    path("suket-penghasilan-tidak-tetap/edit/<int:id>",edit_suketpenghasilantidaktetap,  name="edit_suketpenghasilantidaktetap"),
    path('suket-penghasilan-tidak-tetap/setujui/<int:id>/', setujui_suketpenghasilantidaktetap, name='setujui_suketpenghasilantidaktetap'),
    path('suket-penghasilan-tidak-tetap/tolak/<int:id>/', tolak_suketpenghasilantidaktetap, name='tolak_suketpenghasilantidaktetap'),
    path("suket-penghasilan-tidak-tetap/delete/<int:id>",delete_suketpenghasilantidaktetap,  name="delete_suketpenghasilantidaktetap"),
    path("suket-penghasilan-tidak-tetap/print/<int:id>",print_suketpenghasilantidaktetap,  name="print_suketpenghasilantidaktetap"),
    path("suket-penghasilan-tidak-tetap/detail/<int:id>", detail_suketpenghasilantidaktetap, name="detail_suketpenghasilantidaktetap"),
    path("suket-usaha/",suketusaha,  name="suketusaha"),
    path("suket-usaha/edit/<int:id>",edit_suketusaha,  name="edit_suketusaha"),
    path('suket-usaha/setujui/<int:id>/', setujui_suketusaha, name='setujui_suketusaha'),
    path('suket-usaha/tolak/<int:id>/', tolak_suketusaha, name='tolak_suketusaha'),
    path("suket-usaha/delete/<int:id>",delete_suketusaha,  name="delete_suketusaha"),
    path("suket-usaha/print/<int:id>",print_suketusaha,  name="print_suketusaha"),
    path("suket-usaha/detail/<int:id>", detail_suketusaha, name="detail_suketusaha"),
    path("suket-vaksin-nikah/",suketvaksinnikah,  name="suketvaksinnikah"),
    path("suket-vaksin-nikah/edit/<int:id>",edit_suketvaksinnikah,  name="edit_suketvaksinnikah"),
    path('suket-vaksin-nikah/setujui/<int:id>/', setujui_suketvaksinnikah, name='setujui_suketvaksinnikah'),
    path('suket-vaksin-nikah/tolak/<int:id>/', tolak_suketvaksinnikah, name='tolak_suketvaksinnikah'),
    path("suket-vaksin-nikah/delete/<int:id>",delete_suketvaksinnikah,  name="delete_suketvaksinnikah"),
    path("suket-vaksin-nikah/print/<int:id>",print_suketvaksinnikah,  name="print_suketvaksinnikah"),
    path("suket-vaksin-nikah/detail/<int:id>", detail_suketvaksinnikah, name="detail_suketvaksinnikah"),
    path("suket-pindah-nikah/",suketpindahnikah,  name="suketpindahnikah"),
    path("suket-pindah-nikah/edit/<int:id>",edit_suketpindahnikah,  name="edit_suketpindahnikah"),
    path('suket-pindah-nikah/setujui/<int:id>/', setujui_suketpindahnikah, name='setujui_suketpindahnikah'),
    path('suket-pindah-nikah/tolak/<int:id>/', tolak_suketpindahnikah, name='tolak_suketpindahnikah'),
    path("suket-pindah-nikah/delete/<int:id>",delete_suketpindahnikah,  name="delete_suketpindahnikah"),
    path("suket-pindah-nikah/print/<int:id>",print_suketpindahnikah,  name="print_suketpindahnikah"),
    path("suket-pindah-nikah/detail/<int:id>", detail_suketpindahnikah, name="detail_suketpindahnikah"),
    path("suket-rekomendasi-kelompok-tani/",suketrekkeltani,  name="suketrekkeltani"),
    path("suket-rekomendasi-kelompok-tani/edit/<int:id>",edit_suketrekkeltani,  name="edit_suketrekkeltani"),
    path('suket-rek-kel-tani/setujui/<int:id>/', setujui_suketrekeltani, name='setujui_suketrekeltani'),
    path('suket-rek-kel-tani/tolak/<int:id>/', tolak_suketrekeltani, name='tolak_suketrekeltani'),
    path("suket-rekomendasi-kelompok-tani/delete/<int:id>",delete_suketrekkeltani,  name="delete_suketrekkeltani"),
    path("suket-rekomendasi-kelompok-tani/print/<int:id>",print_suketrekkeltani,  name="print_suketrekkeltani"),
    path("suket-rekomendasi-kelompok-tani/detail/<int:id>", detail_suketrekkeltani, name="detail_suketrekkeltani"),
    path("tambah-pengumuman/", pengumuman, name="pengumuman"),
    path("tambah-pengumuman/edit/<int:id>", edit_pengumuman, name="edit_pengumuman"),
    path("tambah-pengumuman/delete/<int:id>", delete_pengumuman, name="delete_pengumuman"),
    path("tambah-blog/", blog, name="blog"),
    path("tambah-blog/edit/<int:id>", edit_blog, name="edit_blog"),
    path("tambah-blog/delete/<int:id>", delete_blog, name="delete_blog"),
    path("logout/", logoutPage, name="logout"),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('daftar-user/', daftaruser, name='daftar_user'),
    path('daftar-user/edit/<int:id>', edituser, name='edit_user'),
    path('daftar-user/delete/<int:id>', hapususers, name='hapus_user'),
    path('daftar-user/detail/<int:id>', detailuser, name='detail_user'),
    path('pengaduan-asing/', datapengaduanasing, name='pengaduan_asing'),
    path('pengaduan-asing/detail/<int:id>', detailpengaduanasing, name='detail_pengaduan_asing'),
    path('pengaduan-asing/delete/<int:id>', deletepengaduanasing, name='delete_pengaduan_asing'),
    path('register-admin/', register_super_admin, name='register_super_admin'),
    
    
    
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)