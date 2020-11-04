from django import forms
from books_app.models import books_db

class bookform(forms.ModelForm):
      class Meta():
         model=books_db
         fields=["title","pages"] 