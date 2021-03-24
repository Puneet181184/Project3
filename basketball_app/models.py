from django.db import models


# Create your models here.
class  basketball_db(models.Model):
   name=models.CharField(max_length=512,null=True)
   age=models.CharField(max_length=512,null=True)
   dob=models.CharField(max_length=512,null=True)
   nationality=models.CharField(max_length=512,null=True)
   college=models.CharField(max_length=512,null=True)
   position=models.CharField(max_length=512,null=True)
   height=models.CharField(max_length=512,null=True)
   weight=models.CharField(max_length=512,null=True)
   preferedhand=models.CharField(max_length=512,null=True)
   games=models.CharField(max_length=512,null=True)
   gamestarted=models.CharField(max_length=512,null=True)
   minutes=models.CharField(max_length=512,null=True)
   goals=models.CharField(max_length=512,null=True)
   attempts=models.CharField(max_length=512,null=True)
   assists=models.CharField(max_length=512,null=True)
   steals=models.CharField(max_length=512,null=True)
   points=models.CharField(max_length=512,null=True)
   threepoints=models.CharField(max_length=512,null=True)
   twopoints=models.CharField(max_length=512,null=True)
   blocks=models.CharField(max_length=512,null=True)
   freethrows=models.CharField(max_length=512,null=True)
   rebounds=models.CharField(max_length=512,null=True)
   fouls=models.CharField(max_length=512,null=True)











