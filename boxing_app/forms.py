from django import forms
from boxing_app.models import boxing_db

class playerform(forms.ModelForm):
      class Meta():
         model=boxing_db
         fields=["name","age","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=boxing_db
         fields=["name","height","weight"] 
class pointstatsform(forms.ModelForm):
      class Meta():
         model=boxing_db
         fields=["name","wins","losses","draws"]   
class searchform(forms.ModelForm):
      class Meta():
         model=boxing_db
         fields=["name"]                                             