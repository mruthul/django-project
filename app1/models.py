from django.db import models

# Create your models here.
class Signup(models.Model):
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Email=models.EmailField()
    Password=models.CharField(max_length=8)

class Image(models.Model):
    Name=models.CharField(max_length=20)
    Img=models.ImageField(upload_to='pics/',null=True,blank=True)
    Brand=models.CharField(max_length=20)
    Year=models.IntegerField()