from django import forms
from tennis_app.models import tennis_db

class playerform(forms.ModelForm):
      class Meta():
         model=tennis_db
         fields=["name","age","dob","nationality"]

class aboutform(forms.ModelForm):
      class Meta():
         model=tennis_db
         fields=["name","rank","debut"]

class detailsform(forms.ModelForm):
      class Meta():
         model=tennis_db
         fields=["name","seasons","height","weight","preferedhand"]

class careerstatsform(forms.ModelForm):
      class Meta():
         model=tennis_db
         fields=["name","titles","grandslams","tourfinals","masters","daviscups"]

class pointstatsform(forms.ModelForm):
      class Meta():
         model=tennis_db
         fields=["name","totalpoints","tournamentpoints","rankingpoints"]

class winstatsform(forms.ModelForm):
      class Meta():
         model=tennis_db
         fields=["name","overallwins","hardwins","claywins","grasswins","carpetwins"]

class gamestatsform(forms.ModelForm):
      class Meta():
         model=tennis_db
         fields=["name","games","aces","faults"]

                                             
