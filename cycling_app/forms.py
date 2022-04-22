from django import forms
from cycling_app.models import cycling_db

class playerform(forms.ModelForm):
      class Meta():
         model=cycling_db
         fields=["name","age","dob","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=cycling_db
         fields=["name","debut","gender"] 
class detailsform(forms.ModelForm):
      class Meta():
         model=cycling_db
         fields=["name","rank","height","weight"] 
class gamestatsform(forms.ModelForm):
      class Meta():
         model=cycling_db
         fields=["name","grandtours","classics"]  
class pointstatsform(forms.ModelForm):
      class Meta():
         model=cycling_db
         fields=["name","points","wins"]                                