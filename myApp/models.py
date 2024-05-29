from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser



# Create your models here.
class UserDetail(AbstractUser):
     
    phone    =models.CharField(max_length=20 ,unique=True,null=True)
    password=models.CharField(max_length=100000)
    email= models.EmailField(unique=True)
    cart=       ArrayField(models.BigIntegerField(),null=True ,size=1000)
    for_sale=  ArrayField(models.BigIntegerField() ,null=True,size=1000)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['username']

class Products(models.Model):
    product_name= models.CharField(max_length=200)
    product_price=models.IntegerField()
    product_img_url=models.CharField(max_length=2000)
    seller_detail=models.BigIntegerField()
    description=models.CharField(max_length=200 ,null=True)










