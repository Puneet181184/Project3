from django.db import models

# Create your models here.
class cricket_db(models.Model):
   name=models.CharField(max_length=512,null=True)
   age=models.CharField(max_length=512,null=True)
   country=models.CharField(max_length=512,null=True)
   debut=models.CharField(max_length=512,null=True)
   skill=models.CharField(max_length=512,null=True)
   odimatches=models.CharField(max_length=512,null=True)
   odiruns=models.CharField(max_length=512,null=True)
   odiwickets=models.CharField(max_length=512,null=True)
   odicatches=models.CharField(max_length=512,null=True)
   testmatches=models.CharField(max_length=512,null=True)
   testruns=models.CharField(max_length=512,null=True)
   testwickets=models.CharField(max_length=512,null=True)
   testcatches=models.CharField(max_length=512,null=True)
   t20matches=models.CharField(max_length=512,null=True)
   t20runs=models.CharField(max_length=512,null=True)
   t20wickets=models.CharField(max_length=512,null=True)
   t20catches=models.CharField(max_length=512,null=True)




