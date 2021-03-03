from django import forms
from chess_app.models import chess_db

class playerform(forms.ModelForm):
      class Meta():
         model=chess_db
         fields=["name","age","dob","nationality"]
class aboutform(forms.ModelForm):
      class Meta():
         model=chess_db
         fields=["rank","debut"]
class detailsform(forms.ModelForm):
      class Meta():
         model=chess_db
         fields=["height","weight"] 
class personalstatsform(forms.ModelForm):
      class Meta():
         model=chess_db
         fields=["title","playerid","gender"]
class ratingstatsform(forms.ModelForm):
      class Meta():
         model=chess_db
         fields=["stdrating","rapidrating","blitzrating"]
class gamestatsform(forms.ModelForm):
      class Meta():
         model=chess_db
         fields=["games","wins","draws","losses","score"]                                   
         