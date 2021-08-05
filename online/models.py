from django.db import models

# Create your models here.
class Category(models.Model):
    age=(("KIDS","Kids"),("ADULTS","adults"))
    #CAT_ID= models.IntegerField(primary_key=True)
    cat_name = models.CharField(max_length=25)
    agegroup = models.CharField(max_length=30, choices=age, default=("kids"))
    specialoffer = models.CharField(max_length=100)
    
    
class Flipkart(models.Model):
    FID= models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=25)
    price=models.IntegerField()
    discount=models.IntegerField()
    CAT_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    
class Myntra(models.Model):
    MID= models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=25)
    price=models.IntegerField()
    discount=models.IntegerField()
    CAT_id=models.ForeignKey(Category, on_delete=models.CASCADE)
    
class Customer(models.Model):
    Cid= models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=25)
    phone=models.BigIntegerField()
    address=models.TextField(max_length=100)
    FID=models.ForeignKey(Flipkart, on_delete=models.CASCADE)
    MID=models.ForeignKey(Myntra, on_delete=models.CASCADE)
    
    
    
    
    