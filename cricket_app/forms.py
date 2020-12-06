from django import forms
from cricket_app.models import cricket_db

class playerform(forms.ModelForm):
      class Meta():
         model=cricket_db
         fields=["name","age","country"] 

class aboutform(forms.ModelForm):
      class Meta():
         model=cricket_db
         fields=["name","debut","skill"]          

class odistatsform(forms.ModelForm):
      class Meta():
         model=cricket_db
         fields=["name","odimatches","odiruns","odiwickets","odicatches"]

class teststatsform(forms.ModelForm):
      class Meta():
         model=cricket_db
         fields=["name","testmatches","testruns","testwickets","testcatches"]         
class t20statsform(forms.ModelForm):
      class Meta():
         model=cricket_db
         fields=["name","t20matches","t20runs","t20wickets","t20catches"]


class searchform(forms.ModelForm):
      class Meta():
         model=cricket_db
         fields=["name"]   