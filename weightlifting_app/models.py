from django.db import models


# Create your models here.
class  weightlifting_db(models.Model):
   name=models.CharField(max_length=512,null=True)
   age=models.CharField(max_length=512,null=True)
   dob=models.CharField(max_length=512,null=True)
   country=models.CharField(max_length=512,null=True)
   gender=models.CharField(max_length=512,null=True)
   category=models.CharField(max_length=512,null=True)
   rank=models.CharField(max_length=512,null=True)
   height=models.CharField(max_length=512,null=True)
   weight=models.CharField(max_length=512,null=True)
   snatch=models.CharField(max_length=512,null=True)
   jerk=models.CharField(max_length=512,null=True)
   total=models.CharField(max_length=512,null=True)
   
   
   


