from django import forms
from rowing_app.models import rowing_db

class playerform(forms.ModelForm):
      class Meta():
         model=rowing_db
         fields=["name","age","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=rowing_db
         fields=["name","height","weight"]                         
class searchform(forms.ModelForm):
      class Meta():
         model=rowing_db
         fields=["name"]              