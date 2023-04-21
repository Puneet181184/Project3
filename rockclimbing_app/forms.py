from django import forms
from rockclimbing_app.models import rockclimbing_db

class playerform(forms.ModelForm):
      class Meta():
         model=rockclimbing_db
         fields=["name","age","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=rockclimbing_db
         fields=["name","height","weight"]  
class pointstatsform(forms.ModelForm):
      class Meta():
         model=archery_db
         fields=["name","rankingboulder","rankinglead"] 
class searchform(forms.ModelForm):
      class Meta():
         model=rockclimbing_db
         fields=["name"]    