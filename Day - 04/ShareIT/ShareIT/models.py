from django.db import models

class Register(models.Model):
    regid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,unique=True)        
    password=models.CharField(max_length=10)
    mobile=models.CharField(max_length=15)
    address = models.CharField(max_length=255, default='Not Provided')
    city=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    status=models.IntegerField()
    role=models.CharField(max_length=10)
    info=models.CharField(max_length=50)
