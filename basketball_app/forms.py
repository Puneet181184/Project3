from django import forms
from basketball_app.models import basketball_db

class playerform(forms.ModelForm):
      class Meta():
         model=basketball_db
         fields=["name","age","dob","nationality"]
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