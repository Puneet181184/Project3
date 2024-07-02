from django.db import models


# Create your models here.
class  skating_db(models.Model):
   name=models.CharField(max_length=512,null=True)
   age=models.CharField(max_length=512,null=True)
   dob=models.CharField(max_length=512,null=True)
   gender=models.CharField(max_length=512,null=True)
   club=models.CharField(max_length=512,null=True)
   
   






