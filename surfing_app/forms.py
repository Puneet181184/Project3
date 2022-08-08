from django import forms
from surfing_app.models import surfing_db

class playerform(forms.ModelForm):
      class Meta():
         model=surfing_db
         fields=["name","age","dob","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=surfing_db
         fields=["name","gender","height","weight"]
class detailsform(forms.ModelForm):
      class Meta():
         model=surfing_db
         fields=["name","rank","debut"]                  
class pointstatsform(forms.ModelForm):
      class Meta():
         model=surfing_db
         fields=["name","wins","score"]         
class searchform(forms.ModelForm):
      class Meta():
         model=surfing_db
         fields=["name"]                       