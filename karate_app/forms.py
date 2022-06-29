from django import forms
from karate_app.models import karate_db

class playerform(forms.ModelForm):
      class Meta():
         model=karate_db
         fields=["name","age","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=karate_db
         fields=["name","gender"]  
class detailsform(forms.ModelForm):
      class Meta():
         model=karate_db
         fields=["name","rank","category"] 
class pointstatsform(forms.ModelForm):
      class Meta():
         model=karate_db
         fields=["name","worldgold","worldsilver","worldbronze"]                        