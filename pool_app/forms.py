from django import forms
from pool_app.models import pool_db

class playerform(forms.ModelForm):
      class Meta():
         model=pool_db
         fields=["name","age","dob","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=pool_db
         fields=["name","gender"] 
class detailsform(forms.ModelForm):
      class Meta():
         model=pool_db
         fields=["name","rank","wpanumber"] 
class pointsstatsform(forms.ModelForm):
      class Meta():
         model=pool_db
         fields=["name","usopenpoints","austriaopenpoints"] 
class careerstatsform(forms.ModelForm):
      class Meta():
         model=pool_db
         fields=["name","worldcuppoints","totalpoints"]                                 