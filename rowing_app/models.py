from django.db import models


# Create your models here.
class  rowing_db(models.Model):
   name=models.CharField(max_length=512,null=True)
   age=models.CharField(max_length=512,null=True)
   country=models.CharField(max_length=512,null=True)
   height=models.CharField(max_length=512,null=True)
   weight=models.CharField(max_length=512,null=True)
 
   
   
   
