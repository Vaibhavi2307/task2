from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    GENDER=[('male',"Male"),('female',"Female")]
    email = models.EmailField(max_length=255,unique=True)
    contact_no=models.IntegerField()
    gender=models.CharField(max_length=20,choices=GENDER)
    address=models.TextField()
    landmark=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    pincode=models.CharField(max_length=20)





