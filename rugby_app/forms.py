from django import forms
from rugby_app.models import rugby_db

class playerform(forms.ModelForm):
      class Meta():
         model=rugby_db
         fields=["name","age","dob","nationality"]
class aboutform(forms.ModelForm):
      class Meta():
         model=rugby_db
         fields=["name","team","position"]
class detailsform(forms.ModelForm):
      class Meta():
         model=rugby_db
         fields=["name","debut","height","weight"] 
class matchstatsform(forms.ModelForm):
      class Meta():
         model=rugby_db
         fields=["name","matches","wins","draws","losses"] 
class gamestatsform(forms.ModelForm):
      class Meta():
         model=rugby_db
         fields=["name","minutes","started"] 
class pointstatsform(forms.ModelForm):
      class Meta():
         model=rugby_db
         fields=["name","points","tries","drops","penalties","conversions"]
class cardstatsform(forms.ModelForm):
      class Meta():
         model=rugby_db
         fields=["name","yellowcards","redcards"]         
