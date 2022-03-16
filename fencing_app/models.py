from django.db import models


# Create your models here.
class  fencing_db(models.Model):
   name=models.CharField(max_length=512,null=True)
   age=models.CharField(max_length=512,null=True)
   dob=models.CharField(max_length=512,null=True)
   country=models.CharField(max_length=512,null=True)
   debut=models.CharField(max_length=512,null=True)
   gender=models.CharField(max_length=512,null=True)
   rank=models.CharField(max_length=512,null=True)
   style=models.CharField(max_length=512,null=True)
   points=models.CharField(max_length=512,null=True)
   hand=models.CharField(max_length=512,null=True)
   worldcupgold=models.CharField(max_length=512,null=True)
   worldcupsilver=models.CharField(max_length=512,null=True)
   worldcupbronze=models.CharField(max_length=512,null=True)
   
   
