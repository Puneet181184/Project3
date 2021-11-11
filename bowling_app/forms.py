from django import forms
from bowling_app.models import bowling_db

class playerform(forms.ModelForm):
      class Meta():
         model=bowling_db
         fields=["name","age","country"]