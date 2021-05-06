from django.db import models
from django.contrib.auth.models import User

class Pincode(models.Model):
    pincode = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    
    def _str_(self):
        return self.pincode

class Address(models.Model):
    phone = models.CharField(max_length=50)
    address = models.TextField(max_length=500, null=True)
    pincode = models.ForeignKey(Pincode,null=True,on_delete=models.CASCADE)

    def _str_(self):
        return self.phone

class Authentication(models.Model):
    is_customer = models.BooleanField(default=False)
    is_farmer = models.BooleanField(default=False)
    user_id= models.ForeignKey(User,on_delete=models.CASCADE)
    
    def _str_(self):
        return self.user_id
