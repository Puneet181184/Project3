from django import forms
from lacrosse_app.models import lacrosse_db

class playerform(forms.ModelForm):
      class Meta():
         model=lacrosse_db
         fields=["name","age","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=lacrosse_db
         fields=["name","height","weight"] 
class pointstatsform(forms.ModelForm):
      class Meta():
         model=lacrosse_db
         fields=["name","rank"] 
class searchform(forms.ModelForm):
      class Meta():
         model=lacrosse_db
         fields=["name"]                                             