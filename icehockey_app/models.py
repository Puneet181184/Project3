from django.db import models


# Create your models here.
class  icehockey_db(models.Model):
   name=models.CharField(max_length=512,null=True)
   age=models.CharField(max_length=512,null=True)
   dob=models.CharField(max_length=512,null=True)
   nationality=models.CharField(max_length=512,null=True)
   team=models.CharField(max_length=512,null=True)
   position=models.CharField(max_length=512,null=True)
   debut=models.CharField(max_length=512,null=True)
   height=models.CharField(max_length=512,null=True)
   weight=models.CharField(max_length=512,null=True)
   games=models.CharField(max_length=512,null=True)
   assists=models.CharField(max_length=512,null=True)
   points=models.CharField(max_length=512,null=True)
   penaltyminutes=models.CharField(max_length=512,null=True)
   goals=models.CharField(max_length=512,null=True)
   powerplaygoals=models.CharField(max_length=512,null=True)
   shorthandgoals=models.CharField(max_length=512,null=True)
   powerplaypoints=models.CharField(max_length=512,null=True)
   shorthandpoints=models.CharField(max_length=512,null=True)
   wininggoals=models.CharField(max_length=512,null=True)
   overtimegoals=models.CharField(max_length=512,null=True)
   shots=models.CharField(max_length=512,null=True)
   shotspercentage=models.CharField(max_length=512,null=True)
   winspercentage=models.CharField(max_length=512,null=True)
   






