from django.db import models


# Create your models here.
class  polo_db(models.Model):
   name=models.CharField(max_length=512,null=True)
   age=models.CharField(max_length=512,null=True)
   country=models.CharField(max_length=512,null=True)
   status=models.CharField(max_length=512,null=True)
   points=models.CharField(max_length=512,null=True)
   
   
