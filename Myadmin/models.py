from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Categorie(models.Model):
    catname = models.CharField(max_length=20)

    def __str__(self):
        return self.catname

    class Meta:
        db_table="Categories"


class Cake(models.Model):
    cakename=models.CharField(max_length=20)
    description=models.CharField(max_length=20)
    price=models.FloatField(default=199)
    imageurl=models.ImageField(upload_to='images/',default='abc.jpg')
    category=models.ForeignKey(Categorie,on_delete=models.CASCADE)

    class Meta:
        db_table = "Cake"
    
