
from django.db import models


# Create your models here.
class  rockclimbing_db(models.Model):
   name=models.CharField(max_length=512,null=True)
   age=models.CharField(max_length=512,null=True)
   country=models.CharField(max_length=512,null=True)
   height=models.CharField(max_length=512,null=True)
   weight=models.CharField(max_length=512,null=True)
   rankingboulder=models.CharField(max_length=512,null=True)
   rankinglead=models.CharField(max_length=512,null=True)
  