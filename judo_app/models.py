from django.db import models


# Create your models here.
class  judo_db(models.Model):
   name=models.CharField(max_length=512,null=True)
   age=models.CharField(max_length=512,null=True)
   country=models.CharField(max_length=512,null=True)
   rank=models.CharField(max_length=512,null=True)
   points=models.CharField(max_length=512,null=True)
   gold=models.CharField(max_length=512,null=True)
   silver=models.CharField(max_length=512,null=True)
   bronze=models.CharField(max_length=512,null=True)
   
