from django import forms
from surfing_app.models import surfing_db

class playerform(forms.ModelForm):
      class Meta():
         model=surfing_db
         fields=["name","age","dob","country"]