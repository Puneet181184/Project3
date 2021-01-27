from django.db import models

# Create your models here.
class tennis_db(models.Model):
   name=models.CharField(max_length=512,null=True)
   age=models.CharField(max_length=512,null=True)
   dob=models.CharField(max_length=512,null=True)
   nationality=models.CharField(max_length=512,null=True)
   rank=models.CharField(max_length=512,null=True)
   debut=models.CharField(max_length=512,null=True)
   seasons=models.CharField(max_length=512,null=True)
   height=models.CharField(max_length=512,null=True)
   weight=models.CharField(max_length=512,null=True)
   preferedhand=models.CharField(max_length=512,null=True)
   titles=models.CharField(max_length=512,null=True)
   grandslams=models.CharField(max_length=512,null=True)
   tourfinals=models.CharField(max_length=512,null=True)
   masters=models.CharField(max_length=512,null=True)
   daviscups=models.CharField(max_length=512,null=True)
   totalpoints=models.CharField(max_length=512,null=True)
   tournamentpoints=models.CharField(max_length=512,null=True)
   rankingpoints=models.CharField(max_length=512,null=True)
   overallwins=models.CharField(max_length=512,null=True)
   hardwins=models.CharField(max_length=512,null=True)
   claywins=models.CharField(max_length=512,null=True)
   grasswins=models.CharField(max_length=512,null=True)
   carpetwins=models.CharField(max_length=512,null=True)
   games=models.CharField(max_length=512,null=True)
   aces=models.CharField(max_length=512,null=True)
   faults=models.CharField(max_length=512,null=True)











