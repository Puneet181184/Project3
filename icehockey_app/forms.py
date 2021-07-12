from django import forms
from icehockey_app.models import icehockey_db

class playerform(forms.ModelForm):
      class Meta():
         model=icehockey_db
         fields=["name","age","dob","nationality"]
class aboutform(forms.ModelForm):
      class Meta():
         model=icehockey_db
         fields=["name","team","position"]
class detailsform(forms.ModelForm):
      class Meta():
         model=icehockey_db
         fields=["name","debut","height","weight"] 
class gamestatsform(forms.ModelForm):
      class Meta():
         model=icehockey_db
         fields=["name","games","assists"]
class goalstatsform(forms.ModelForm):
      class Meta():
         model=icehockey_db
         fields=["name","goals","powerplaygoals","shorthandgoals","wininggoals","overtimegoals"]                                   
class pointstatsform(forms.ModelForm):
      class Meta():
         model=icehockey_db
         fields=["name","points","powerplaypoints","shorthandpoints"] 
class shotstatsform(forms.ModelForm):
      class Meta():
         model=icehockey_db
         fields=["name","shots","shotspercentage","penaltyminutes","winspercentage"]                 