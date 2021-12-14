from django import forms
from weightlifting_app.models import weightlifting_db

class playerform(forms.ModelForm):
      class Meta():
         model=weightlifting_db
         fields=["name","age","dob","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=weightlifting_db
         fields=["name","gender","height","weight"]
class detailsform(forms.ModelForm):
      class Meta():
         model=weightlifting_db
         fields=["name","category","rank"]
class careerstatsform(forms.ModelForm):
      class Meta():
         model=weightlifting_db
         fields=["name","snatch","jerk"]
class matchstatsform(forms.ModelForm):
      class Meta():
         model=weightlifting_db
         fields=["name","total"]
