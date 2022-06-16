from django.db import models


# Create your models here.
class  karate_db(models.Model):
   name=models.CharField(max_length=512,null=True)
   age=models.CharField(max_length=512,null=True)
   country=models.CharField(max_length=512,null=True)
   gender=models.CharField(max_length=512,null=True)
   rank=models.CharField(max_length=512,null=True)
   category=models.CharField(max_length=512,null=True)
   worldgold=models.CharField(max_length=512,null=True)
   worldsilver=models.CharField(max_length=512,null=True)
   worldbronze=models.CharField(max_length=512,null=True)
   
   
   


