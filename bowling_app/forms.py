from django import forms
from bowling_app.models import bowling_db

class playerform(forms.ModelForm):
      class Meta():
         model=bowling_db
         fields=["name","age","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=bowling_db
         fields=["name","gender","city","state"]
class detailsform(forms.ModelForm):
      class Meta():
         model=bowling_db
         fields=["name","debut"] 
class careerstatsform(forms.ModelForm):
      class Meta():
         model=bowling_db
         fields=["name","bowls","events","championships"]
class matchstatsform(forms.ModelForm):
      class Meta():
         model=bowling_db
         fields=["name","matches","cashes"] 
class titlestatsform(forms.ModelForm):
      class Meta():
         model=bowling_db
         fields=["name","titles","average"] 
class searchform(forms.ModelForm):
      class Meta():
         model=bowling_db
         fields=["name"]                                                                  