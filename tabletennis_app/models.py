from django.db import models


# Create your models here.
class  tabletennis_db(models.Model):
   name=models.CharField(max_length=512,null=True)
   age=models.CharField(max_length=512,null=True)
   dob=models.CharField(max_length=512,null=True)
   country=models.CharField(max_length=512,null=True)
   gender=models.CharField(max_length=512,null=True)
   debut=models.CharField(max_length=512,null=True)
   height=models.CharField(max_length=512,null=True)
   weight=models.CharField(max_length=512,null=True)
   plays=models.CharField(max_length=512,null=True)
   grip=models.CharField(max_length=512,null=True)
   rank=models.CharField(max_length=512,null=True)
   bestrank=models.CharField(max_length=512,null=True)
   singlesplayed=models.CharField(max_length=512,null=True)
   singleswon=models.CharField(max_length=512,null=True)
   singleslost=models.CharField(max_length=512,null=True)
   doublesplayed=models.CharField(max_length=512,null=True)
   doubleswon=models.CharField(max_length=512,null=True)
   doubleslost=models.CharField(max_length=512,null=True)
   totalplayed=models.CharField(max_length=512,null=True)
   totalwn=models.CharField(max_length=512,null=True)
   totallost=models.CharField(max_length=512,null=True)


