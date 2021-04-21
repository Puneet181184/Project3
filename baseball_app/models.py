from django.db import models


# Create your models here.
class  baseball_db(models.Model):
   name=models.CharField(max_length=512,null=True)
   age=models.CharField(max_length=512,null=True)
   dob=models.CharField(max_length=512,null=True)
   nationality=models.CharField(max_length=512,null=True)
   college=models.CharField(max_length=512,null=True)
   team=models.CharField(max_length=512,null=True)
   position=models.CharField(max_length=512,null=True)
   debut=models.CharField(max_length=512,null=True)
   height=models.CharField(max_length=512,null=True)
   weight=models.CharField(max_length=512,null=True)
   games=models.CharField(max_length=512,null=True)
   appearances=models.CharField(max_length=512,null=True)
   atbats=models.CharField(max_length=512,null=True)
   runs=models.CharField(max_length=512,null=True)
   hits=models.CharField(max_length=512,null=True)
   doubles=models.CharField(max_length=512,null=True)
   triples=models.CharField(max_length=512,null=True)
   homeruns=models.CharField(max_length=512,null=True)
   runsbatted=models.CharField(max_length=512,null=True)
   steals=models.CharField(max_length=512,null=True)
   walks=models.CharField(max_length=512,null=True)
   strikeouts=models.CharField(max_length=512,null=True)
   stolenbases=models.CharField(max_length=512,null=True)
   totalbases=models.CharField(max_length=512,null=True)
   caughtstealing=models.CharField(max_length=512,null=True)




