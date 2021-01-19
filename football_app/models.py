from django.db import models

# Create your models here.
class football_db(models.Model):
   name=models.CharField(max_length=512,null=True)
   age=models.CharField(max_length=512,null=True)
   dob=models.CharField(max_length=512,null=True)
   nationality=models.CharField(max_length=512,null=True)
   birthplace=models.CharField(max_length=512,null=True)
   fifaid=models.CharField(max_length=512,null=True)
   debut=models.CharField(max_length=512,null=True)
   position=models.CharField(max_length=512,null=True)
   league=models.CharField(max_length=512,null=True)
   club=models.CharField(max_length=512,null=True)
   height=models.CharField(max_length=512,null=True)
   weight=models.CharField(max_length=512,null=True)
   foot=models.CharField(max_length=512,null=True)
   matches=models.CharField(max_length=512,null=True)
   goals=models.CharField(max_length=512,null=True)
   assists=models.CharField(max_length=512,null=True)
   penaltyscored=models.CharField(max_length=512,null=True)
   penaltymissed=models.CharField(max_length=512,null=True)
   goalsconceded=models.CharField(max_length=512,null=True)
   yellowcards=models.CharField(max_length=512,null=True)
   redcards=models.CharField(max_length=512,null=True)






