from django import forms
from karate_app.models import karate_db

class playerform(forms.ModelForm):
      class Meta():
         model=karate_db
         fields=["name","age","country"]