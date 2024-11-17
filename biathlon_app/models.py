from django.db import models

# Create your models here.
class biathlon_db(models.Model):
   name=models.CharField(max_length=512,null=True)
   dob=models.CharField(max_length=512,null=True)
   country=models.CharField(max_length=512,null=True)
   gender=models.CharField(max_length=512,null=True)
   rank=models.CharField(max_length=512,null=True)
   points=models.CharField(max_length=512,null=True)
   



