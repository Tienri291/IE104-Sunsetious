
from django.db import models
from django.contrib.auth.models import User

from django.core.validators import RegexValidator


#class ADMIN(models.Model):
#     MaAM = models.CharField(max_length=10, primary_key=True)
#     HoTen = models.CharField(max_length=30)
#     Email = models.CharField()
#     Username = models.CharField()
# #     Password = models.CharField()

# class emailnhandeal(models.Model):
#     email = models.CharField(max_length=50)

# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
#     fullname = models.CharField(max_length=30)
#     email = models.CharField(max_length=30)
#     username = models.CharField(max_length=15)
#     password = models.CharField(max_length=16)

# class Customer(User):
#     fullname = models.CharField(max_length=30)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=12, blank=True, null=True) # validators should be a list

    def __str__(self):
        return self.name

class Product(models.Model):
    slug = models.SlugField(unique=True, blank=True)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    stars = models.DecimalField(max_digits=5, decimal_places=1)
    n_reviews = models.IntegerField()
    image = models.ImageField(null=True, blank=True)
    views = models.IntegerField()
    location = models.CharField(max_length=30)
    duration = models.IntegerField(default=1)
    detail_info = models.TextField(blank=True, null=True)
    info_dd = models.TextField(blank=True, null=True)
    n_orders = models.IntegerField(default=0)
    

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Room(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    stars = models.DecimalField(max_digits=5, decimal_places=1)
    n_reviews = models.IntegerField()
    image = models.ImageField(null=True, blank=True)
    views = models.IntegerField()
    location = models.CharField(max_length=30)
    

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Area(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(null=True, blank=True)   

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Voucher(models.Model):
    code = models.CharField(max_length=40)
    expiration_date = models.DateField()
    value = models.DecimalField(max_digits=3, decimal_places=2)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    voucher = models.ForeignKey(Voucher, on_delete=models.SET_NULL, blank=True, null=True)

    @property
    def get_total(self):
        total = (self.product.price * self.quantity) * (1.1 - self.voucher.value)
        return total
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    order_item = models.ForeignKey(OrderItem, on_delete=models.SET_NULL, blank=True, null=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True)
    payment_option = models.CharField(max_length=10, null=True, blank=True)
    
    def __str__(self):
        return str(self.id)


    # def get_cart_total(self):
    #     orderitems = self.orderitem_set.all()
    #     total = sum([item.get_total for item in orderitems])
    #     return total

    # def get_cart_items(self):
    #     orderitems = self.orderitem_set.all()
    #     total = sum([item.quantity for item in orderitems])
    #     return total

class Move(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    stars = models.DecimalField(max_digits=5, decimal_places=1)
    n_reviews = models.IntegerField()
    image = models.ImageField(null=True, blank=True)
    views = models.IntegerField()
    location = models.CharField(max_length=30)
    

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

#class DANHMUC (models.Model):
#     MaDM = models.CharField(max_length=10, primary_key=True)
#     TenDM = models.CharField()


#class SANPHAM (models.Model):
#     MaSP = models.CharField(max_length=10, primary_key=True)
#     TenSP = models.CharField(max_length=30)
#     MaDM = models.ForeignKey(DANHMUC, verbose_name=(""), on_delete=models.CASCADE)
#     GiaGoc = models.FloatField()
#     GiaGiam = models.FloatField()
#     Image_list = models.Imageprice = models.IntegerField()
#     DanhGia = models.CharField()
#     LuotXem = models.Count()
#     Slug = models.SlugField()
#     Mota = models.CharField()


# class DONHANG (models.Model):
#     MaDH = models.CharField(max_length=10, primary_key=True)
#     TenDH = models.CharField(max_length=100)
#     MaSP = models.ForeignKey(SANPHAM, verbose_name=(""), on_delete=models.CASCADE)
#     MaDM = models.ForeignKey(DANHMUC, verbose_name=_(""), on_delete=models.CASCADE)
#     NgayBD = models.DateTimeField(auto_now_add=True)
#     DonGia = models.FloatField()
#     MaGiamGia = models.CharField(max_length=10)

# class GIOHANG (models.Model):
#     MaKH = models.CharField(max_length=10, primary_key=True)
#     MaDH = models.CharField(max_length=10, primary_key=True)
#     HoTen = models.CharField(max_length=30)
#     NgayThem = models.DateTimeField(auto_now_add=True)
#     CapNhatNgayThem = models.DateTimeField(auto_now_add=True)
#     TongTien = models.FloatField()

# class MAGIAMGIA (models.Model):
#     MaGG = models.CharField(max_length=15, primary_key=True)
#     TenMa = models.CharField(max_length=15)
#     PhanTramGiam = models.IntegerField()

# class CTHD (models.Model):
#     MaSP = models.CharField(SANPHAM,max_length=10, primary_key=True)
#     MaDH = models.CharField(DONHANG, max_length=10, primary_key=True)

# class GG_DH (models.Model):
#     MaGG = models.CharField(MAGIAMGIA,max_length=15, primary_key=True)
#     MaDH = models.CharField(DONHANG, max_length=10, primary_key=True)

# class GH_SP (models.Model):
#     MaKH = models.CharField(KHACHHANG,max_length=10, primary_key=True)
#     MaSP = models.CharField(SANPHAM,max_length=10, primary_key=True)

