from django.db import models

# Create your models here.
class books_db(models.Model):
   title=models.CharField(max_length=512,null=True)
   pages=models.CharField(max_length=512,null=True)
   author=models.CharField(max_length=512,null=True)
   publisher=models.CharField(max_length=512,null=True)
   isbn=models.CharField(max_length=512,null=True)
   year=models.CharField(max_length=512,null=True)
   price=models.CharField(max_length=512,null=True)
