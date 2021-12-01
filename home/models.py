from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

# Em code xong phần database rồi nha!!!

class ADMIN(models.Model):
MaAM = models.CharField(max_length=10, primary_key=True)
HoTen = models.CharField(max_length=30)
Email = models.CharField()
Username = models.CharField()
Password = models.CharField()



class KHACHHANG (models.Model):
MaKH = models.CharField(max_length=10, primary_key=True)
HoTen = models.CharField(max_length=30)
Email = models.CharField()
Username = models.CharField(max_lenght=15)
Password = models.CharField(max_length=16)



class DANHMUC (models.Model):
MaDM = models.CharField(max_length=10, primary_key=True)
TenDM = models.CharField()




class SANPHAM (models.Model):
MaSP = models.CharField(max_length=10, primary_key=True)
TenSP = models.CharField(max_length=30)
MaDM = models.ForeignKey(DANHMUC, verbose_name=(""), on_delete=models.CASCADE)
GiaGoc = models.FloatField()
GiaGiam = models.FloatField()
Image_list = models.ImageField()
DanhGia = models.CharField()
LuotXem = models.Count()
Slug = models.SlugField()
Mota = models.CharField()




class DONHANG (models.Model):
MaDH = models.CharField(max_length=10, primary_key=True)
TenDH = models.CharField(max_length=100)
MaSP = models.ForeignKey(SANPHAM, verbose_name=(""), on_delete=models.CASCADE)
MaDM = models.ForeignKey(DANHMUC, verbose_name=_(""), on_delete=models.CASCADE)
NgayBD = models.DateTimeField(auto_now_add=True)
DonGia = models.FloatField()
MaGiamGia = models.CharField(max_length=10)



class GIOHANG (models.Model):
MaKH = models.CharField(max_length=10, primary_key=True)
MaDH = models.CharField(max_length=10, primary_key=True)
HoTen = models.CharField(max_length=30)
NgayThem = models.DateTimeField(auto_now_add=True)
CapNhatNgayThem = models.DateTimeField(auto_now_add=True)
TongTien = models.FloatField()



class MAGIAMGIA (models.Model):
MaGG = models.CharField(max_length=15, primary_key=True)
TenMa = models.CharField(max_length=15)
PhanTramGiam = models.IntegerField()



class CTHD (models.Model):
MaSP = models.CharField(SANPHAM,max_length=10, primary_key=True)
MaDH = models.CharField(DONHANG, max_length=10, primary_key=True)



class GG_DH (models.Model):
MaGG = models.CharField(MAGIAMGIA,max_length=15, primary_key=True)
MaDH = models.CharField(DONHANG, max_length=10, primary_key=True)



class GH_SP (models.Model):
MaKH = models.CharField(KHACHHANG,max_length=10, primary_key=True)
MaSP = models.CharField(SANPHAM,max_length=10, primary_key=True)

