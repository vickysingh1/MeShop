from django.db import models

# Create your models here.
class Product(models.Model):
    productid=models.AutoField
    productname=models.CharField(max_length=50)
    category=models.CharField(max_length=50, default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=500)
    pubdate=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.productname


class Contact(models.Model):
    messageid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default='')
    email=models.CharField(max_length=70,default='')
    phone=models.CharField(max_length=70,default='')
    desc=models.CharField(max_length=1000,default="")


    def __str__(self):
        return self.email


class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=100)



    def __str__(self):
        return str(self.order_id)

class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=5000)
    timestamp=models.DateField(auto_now_add=True)


    def __str__(self):
        return str(self.order_id)
    


