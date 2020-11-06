from django import forms
from books_app.models import books_db

class bookform(forms.ModelForm):
      class Meta():
         model=books_db
         fields=["title","pages"] 

class authorform(forms.ModelForm):
      class Meta():
         model=books_db
         fields=["author","publisher"]        

class codesform(forms.ModelForm):
      class Meta():
         model=books_db
         fields=["isbn"]           

class otherform(forms.ModelForm):
      class Meta():
         model=books_db
         fields=["year","price"]           