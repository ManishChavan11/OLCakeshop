from Myadmin.models import Cake
from django.db import models

class UserMaster(models.Model):
    username = models.CharField(max_length=10,primary_key=True)
    password = models.CharField(max_length=10)

    class Meta:
        db_table= "UserMaster" 

class MyCart (models.Model):
    cake= models.ForeignKey(Cake,on_delete=models.CASCADE)
    user=  models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    qty= models.IntegerField()
    
    class Meta:
        db_table= "MyCart"

class carddetails(models.Model):
    cardno = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    expiry= models.CharField(max_length=4)
    balance= models.FloatField(default=1000)

    class Meta:
        db_table= "CardDetails"