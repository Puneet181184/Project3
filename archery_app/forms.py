from django import forms
from archery_app.models import archery_db

class playerform(forms.ModelForm):
      class Meta():
         model=archery_db
         fields=["name","age","dob","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=archery_db
         fields=["name","debut","gender"] 
class detailsform(forms.ModelForm):
      class Meta():
         model=archery_db
         fields=["name","rank"]  
class gamestatsform(forms.ModelForm):
      class Meta():
         model=archery_db
         fields=["name","arrowlength","drawweight","averagearrow"] 
class pointstatsform(forms.ModelForm):
      class Meta():
         model=archery_db
         fields=["name","worldcupgold","worldcupsilver","worldcupbronze"]                                