from django.db import models


# Create your models here.
class  rugby_db(models.Model):
   name=models.CharField(max_length=512,null=True)
   age=models.CharField(max_length=512,null=True)
   dob=models.CharField(max_length=512,null=True)
   nationality=models.CharField(max_length=512,null=True)
   team=models.CharField(max_length=512,null=True)
   position=models.CharField(max_length=512,null=True)
   debut=models.CharField(max_length=512,null=True)
   height=models.CharField(max_length=512,null=True)
   weight=models.CharField(max_length=512,null=True)
   matches=models.CharField(max_length=512,null=True)
   wins=models.CharField(max_length=512,null=True)
   draws=models.CharField(max_length=512,null=True)
   losses=models.CharField(max_length=512,null=True)
   minutes=models.CharField(max_length=512,null=True)
   started=models.CharField(max_length=512,null=True)
   points=models.CharField(max_length=512,null=True)
   tries=models.CharField(max_length=512,null=True)
   drops=models.CharField(max_length=512,null=True)
   penalties=models.CharField(max_length=512,null=True)
   conversions=models.CharField(max_length=512,null=True)
   yellowcards=models.CharField(max_length=512,null=True)
   redcards=models.CharField(max_length=512,null=True)
   





