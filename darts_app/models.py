from django.db import models


# Create your models here.
class  darts_db(models.Model):
   name=models.CharField(max_length=512,null=True)
   age=models.CharField(max_length=512,null=True)
   dob=models.CharField(max_length=512,null=True)
   country=models.CharField(max_length=512,null=True)
   gender=models.CharField(max_length=512,null=True)
   rank=models.CharField(max_length=512,null=True)
   height=models.CharField(max_length=512,null=True)
   darts=models.CharField(max_length=512,null=True)
   titles=models.CharField(max_length=512,null=True)
   finishes=models.CharField(max_length=512,null=True)
  
   
   
   



