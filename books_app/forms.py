from django import forms
from books_app.models import books_db

class bookform(forms.ModelForm):
      class Meta():
         model=books_db
         fields=["title","pages"] 

class authorform(forms.ModelForm):
      class Meta():
         model=books_db
         fields=["title","author","publisher"]        

class codesform(forms.ModelForm):
      class Meta():
         model=books_db
         fields=["title","isbn"]           

class otherform(forms.ModelForm):
      class Meta():
         model=books_db
         fields=["title","year","price"]

class searchform(forms.ModelForm):
      class Meta():
         model=books_db
         fields=["title"]                    