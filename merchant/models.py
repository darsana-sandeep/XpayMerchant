from django.db import models

# Create your models here.

class MerchantProfile(models.Model):
    shop_name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    proof = models.CharField(max_length=100)
    licence = models.IntegerField()
    gst = models.IntegerField()
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    alt_phone = models.IntegerField()
    Email = models.EmailField(max_length=100)
    business_email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
