from django import forms
from horseracing_app.models import horseracing_db

class playerform(forms.ModelForm):
      class Meta():
         model=horseracing_db
         fields=["name","age"]
class aboutform(forms.ModelForm):
      class Meta():
         model=horseracing_db
         fields=["name","rank"] 
class detailsform(forms.ModelForm):
      class Meta():
         model=horseracing_db
         fields=["name","horse","starts"]   
class pointstatsform(forms.ModelForm):
      class Meta():
         model=archery_db
         fields=["name","gold","silver","bronze"] 
class searchform(forms.ModelForm):
      class Meta():
         model=horseracing_db
         fields=["name"]                                             