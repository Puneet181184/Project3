from django import forms
from swimming_app.models import swimming_db

class playerform(forms.ModelForm):
      class Meta():
         model=swimming_db
         fields=["name","age","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=basketball_db
         fields=["name","college","position"] 
class detailsform(forms.ModelForm):
      class Meta():
         model=basketball_db
         fields=["name","height","weight","preferedhand"] 
class gamestatsform(forms.ModelForm):
      class Meta():
         model=basketball_db
         fields=["name","games","gamestarted","minutes"]  
class goalstatsform(forms.ModelForm):
      class Meta():
         model=basketball_db
         fields=["name","goals","attempts","assists","steals"] 
class pointstatsform(forms.ModelForm):
      class Meta():
         model=basketball_db
         fields=["name","points","threepoints","twopoints"] 
class blockstatsform(forms.ModelForm):
      class Meta():
         model=basketball_db
         fields=["name","blocks","freethrows","rebounds","fouls"] 
class searchform(forms.ModelForm):
      class Meta():
         model=basketball_db
         fields=["name"]                  