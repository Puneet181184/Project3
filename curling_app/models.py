from django.db import models


# Create your models here.
class  curling_db(models.Model):
   name=models.CharField(max_length=512,null=True)
   age=models.CharField(max_length=512,null=True)
   country=models.CharField(max_length=512,null=True)
   ranking=models.CharField(max_length=512,null=True)
   
   
   
   



