from django.db import models


# Create your models here.
class  badminton_db(models.Model):
   name=models.CharField(max_length=512,null=True)
   age=models.CharField(max_length=512,null=True)
   dob=models.CharField(max_length=512,null=True)
   country=models.CharField(max_length=512,null=True)
   gender=models.CharField(max_length=512,null=True)
   rank=models.CharField(max_length=512,null=True)
   tourrank=models.CharField(max_length=512,null=True)
   debut=models.CharField(max_length=512,null=True)
   height=models.CharField(max_length=512,null=True)
   weight=models.CharField(max_length=512,null=True)
   plays=models.CharField(max_length=512,null=True)
   careerwins=models.CharField(max_length=512,null=True)
   singlesplayed=models.CharField(max_length=512,null=True)
   singleswon=models.CharField(max_length=512,null=True)
   singleslost=models.CharField(max_length=512,null=True)
   doublesplayed=models.CharField(max_length=512,null=True)
   doubleswon=models.CharField(max_length=512,null=True)
   doubleslost=models.CharField(max_length=512,null=True)
   mixedplayed=models.CharField(max_length=512,null=True)
   mixedwon=models.CharField(max_length=512,null=True)
   mixedlost=models.CharField(max_length=512,null=True)
   
   

