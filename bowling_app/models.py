from django.db import models


# Create your models here.
class  bowling_db(models.Model):
   name=models.CharField(max_length=512,null=True)
   age=models.CharField(max_length=512,null=True)
   country=models.CharField(max_length=512,null=True)
   gender=models.CharField(max_length=512,null=True)
   city=models.CharField(max_length=512,null=True)
   state=models.CharField(max_length=512,null=True)
   debut=models.CharField(max_length=512,null=True)
   bowls=models.CharField(max_length=512,null=True)
   events=models.CharField(max_length=512,null=True)
   championships=models.CharField(max_length=512,null=True)
   matches=models.CharField(max_length=512,null=True)
   cashes=models.CharField(max_length=512,null=True)
   titles=models.CharField(max_length=512,null=True)
   average=models.CharField(max_length=512,null=True)