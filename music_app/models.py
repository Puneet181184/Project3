from django.db import models

# Create your models here.
class music_db(models.Model):
    title=models.CharField(max_length=512,null=True)
    artist=models.CharField(max_length=512,null=True)
    album=models.CharField(max_length=512,null=True)
    country=models.CharField(max_length=512,null=True)
    year=models.CharField(max_length=512,null=True)
    writer=models.CharField(max_length=512,null=True)
    othername=models.CharField(max_length=512,null=True)
    isni=models.CharField(max_length=512,null=True)
    ipi=models.CharField(max_length=512,null=True)
    isrc=models.CharField(max_length=512,null=True)
    sesac_id=models.CharField(max_length=512,null=True)
    sesac_pub=models.CharField(max_length=512,null=True)
    ascap_id=models.CharField(max_length=512,null=True)
    ascap_pub=models.CharField(max_length=512,null=True)
    ascap_ipi=models.CharField(max_length=512,null=True)
    bmi_id=models.CharField(max_length=512,null=True)
    bmi_pub=models.CharField(max_length=512,null=True)
    gmr_id=models.CharField(max_length=512,null=True)
    gmr_pub=models.CharField(max_length=512,null=True)
    gmr_ipi=models.CharField(max_length=512,null=True)
