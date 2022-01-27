from django.db import models


# Create your models here.
class  pool_db(models.Model):
   name=models.CharField(max_length=512,null=True)
   age=models.CharField(max_length=512,null=True)
   dob=models.CharField(max_length=512,null=True)
   country=models.CharField(max_length=512,null=True)
   gender=models.CharField(max_length=512,null=True)
   rank=models.CharField(max_length=512,null=True)
   wpanumber=models.CharField(max_length=512,null=True)
   usopenpoints=models.CharField(max_length=512,null=True)
   austriaopenpoints=models.CharField(max_length=512,null=True)
   worldcuppoints=models.CharField(max_length=512,null=True)
   totalpoints=models.CharField(max_length=512,null=True)
   
   
   


