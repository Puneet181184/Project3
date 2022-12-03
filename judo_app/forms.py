from django import forms
from judo_app.models import judo_db

class playerform(forms.ModelForm):
      class Meta():
         model=judo_db
         fields=["name","age","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=judo_db
         fields=["name","rank"] 
class pointstatsform(forms.ModelForm):
      class Meta():
         model=judo_db
         fields=["name","points","gold","silver","bronze"] 
class searchform(forms.ModelForm):
      class Meta():
         model=judo_db
         fields=["name"]                                                         
                                                            