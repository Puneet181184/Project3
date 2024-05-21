from django.db import models


# Create your models here.
class  skiing_db(models.Model):
   name=models.CharField(max_length=512,null=True)
   age=models.CharField(max_length=512,null=True)
   dob=models.CharField(max_length=512,null=True) 
   height=models.CharField(max_length=512,null=True)
   skitype=models.CharField(max_length=512,null=True)
  
   






