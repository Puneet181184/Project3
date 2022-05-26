from django import forms
from darts_app.models import darts_db

class playerform(forms.ModelForm):
      class Meta():
         model=darts_db
         fields=["name","age","dob","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=darts_db
         fields=["name","gender"]  
class detailsform(forms.ModelForm):
      class Meta():
         model=darts_db
         fields=["name","rank","height"]   
class gamestatsform(forms.ModelForm):
      class Meta():
         model=darts_db
         fields=["name","darts"] 
class pointstatsform(forms.ModelForm):
      class Meta():
         model=darts_db
         fields=["name","titles","finishes"]
class searchform(forms.ModelForm):
      class Meta():
         model=darts_db
         fields=["name"]             
                         


