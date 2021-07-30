from django.db import models


# Create your models here.
class  golf_db(models.Model):
   name=models.CharField(max_length=512,null=True)
   age=models.CharField(max_length=512,null=True)
   dob=models.CharField(max_length=512,null=True)
   country=models.CharField(max_length=512,null=True)
   currentrank=models.CharField(max_length=512,null=True)
   bestrank=models.CharField(max_length=512,null=True)
   debut=models.CharField(max_length=512,null=True)
   height=models.CharField(max_length=512,null=True)
   weight=models.CharField(max_length=512,null=True)
   events=models.CharField(max_length=512,null=True)
   first=models.CharField(max_length=512,null=True)
   second=models.CharField(max_length=512,null=True)
   third=models.CharField(max_length=512,null=True)
   fourth=models.CharField(max_length=512,null=True)
   madecuts=models.CharField(max_length=512,null=True)
   totalpoints=models.CharField(max_length=512,null=True)
   averagepoints=models.CharField(max_length=512,null=True)
   divisor=models.CharField(max_length=512,null=True)
   
   

