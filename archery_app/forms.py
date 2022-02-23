from django import forms
from archery_app.models import archery_db

class playerform(forms.ModelForm):
      class Meta():
         model=archery_db
         fields=["name","age","dob","country"]