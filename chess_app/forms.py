from django import forms
from chess_app.models import chess_db

class playerform(forms.ModelForm):
      class Meta():
         model=chess_db
         fields=["name","age","dob","nationality"]
