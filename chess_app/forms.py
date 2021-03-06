from django import forms
from chess_app.models import chess_db

class playerform(forms.ModelForm):
      class Meta():
         model=chess_db
         fields=["name","age","dob","nationality"]
class aboutform(forms.ModelForm):
      class Meta():
         model=chess_db
         fields=["name","rank","debut"]
class detailsform(forms.ModelForm):
      class Meta():
         model=chess_db
         fields=["name","height","weight"] 
class personalstatsform(forms.ModelForm):
      class Meta():
         model=chess_db
         fields=["name","title","playerid","gender"]
class ratingstatsform(forms.ModelForm):
      class Meta():
         model=chess_db
         fields=["name","stdrating","rapidrating","blitzrating"]
class gamestatsform(forms.ModelForm):
      class Meta():
         model=chess_db
         fields=["name","games","wins","draws","losses","score"]
class searchform(forms.ModelForm):
      class Meta():
         model=chess_db
         fields=["name"]                                                
         