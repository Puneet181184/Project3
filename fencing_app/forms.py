from django import forms
from fencing_app.models import fencing_db

class playerform(forms.ModelForm):
      class Meta():
         model=fencing_db
         fields=["name","age","dob","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=fencing_db
         fields=["name","debut","gender"] 
class detailsform(forms.ModelForm):
      class Meta():
         model=fencing_db
         fields=["name","rank","style"]   
class gamestatsform(forms.ModelForm):
      class Meta():
         model=fencing_db
         fields=["name","hand"] 
class pointstatsform(forms.ModelForm):
      class Meta():
         model=fencing_db
         fields=["name","points","worldcupgold","worldcupsilver","worldcupbronze"]                               