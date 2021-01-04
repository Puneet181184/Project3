from django import forms
from football_app.models import football_db

class playerform(forms.ModelForm):
      class Meta():
         model=football_db
         fields=["name","age","dob","nationality","birthplace"]

class aboutform(forms.ModelForm):
      class Meta():
         model=football_db
         fields=["name","fifaid","debut","position"]

class detaisform(forms.ModelForm):
      class Meta():
         model=football_db
         fields=["name","league","club","height","weight","foot"]

class matchstatsform(forms.ModelForm):
      class Meta():
         model=football_db
         fields=["name","matches"]

class goalstatsform(forms.ModelForm):
      class Meta():
         model=football_db
         fields=["name","goals","assists","goalsconceded"]

class penaltystatsform(forms.ModelForm):
      class Meta():
         model=football_db
         fields=["name","penaltyscored","penaltymissed"]

class cardstatsform(forms.ModelForm):
      class Meta():
         model=football_db
         fields=["name","yellowcards","redcards"]





