from django.db import models

# Create your models here.


class house_details(models.Model):
    name=models.CharField(max_length=1000)
    price=models.IntegerField()
    bedroom=models.CharField(max_length=100)
    description=models.TextField()
    email=models.EmailField(default="")
    # book_image=models.ImageField(upload_to='media/',null=True,blank=True)

class register_details1(models.Model):
    unique_user_code=models.CharField(max_length=1000,default="null")
    is_admin=models.IntegerField(default=0)
    email=models.EmailField()
    password=models.CharField(max_length=100)

class register(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=100,default="null")
    name=models.CharField(max_length=1000)
    phone=models.IntegerField()
    email=models.EmailField()
    last_name=models.CharField(max_length=100)
    # profile_image=models.ImageField(upload_to='media/',null=True,blank=True)

