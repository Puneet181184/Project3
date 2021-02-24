from django.db import models

# Create your models here.
class chess_db(models.Model):
   name=models.CharField(max_length=512,null=True)
   age=models.CharField(max_length=512,null=True)
   dob=models.CharField(max_length=512,null=True)
   nationality=models.CharField(max_length=512,null=True)
   rank=models.CharField(max_length=512,null=True)
   debut=models.CharField(max_length=512,null=True)
   title=models.CharField(max_length=512,null=True)
   playerid=models.CharField(max_length=512,null=True)
   gender=models.CharField(max_length=512,null=True)
   height=models.CharField(max_length=512,null=True)
   weight=models.CharField(max_length=512,null=True)
   stdrating=models.CharField(max_length=512,null=True)
   rapidrating=models.CharField(max_length=512,null=True)
   blitzrating=models.CharField(max_length=512,null=True)
   games=models.CharField(max_length=512,null=True)
   wins=models.CharField(max_length=512,null=True)
   draws=models.CharField(max_length=512,null=True)
   losses=models.CharField(max_length=512,null=True)
   score=models.CharField(max_length=512,null=True)
   











