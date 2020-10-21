from django import forms
from music_app.models import music_db
class newuserform(forms.ModelForm):
  class Meta():
    model=music_db
    fields="__all__" 

class trackform(forms.ModelForm):
  class Meta():
    model=music_db
    fields=["title","album"]
    
class artistform(forms.ModelForm):
  class Meta():
    model=music_db
    fields=["title","artist","writer","othername"]

class codesform(forms.ModelForm):
  class Meta():
    model=music_db
    fields=["title","isni","ipi","isrc"]

class sesacform(forms.ModelForm):
  class Meta():
    model=music_db
    fields=["title","sesac_id","sesac_pub"]

class ascapform(forms.ModelForm):
  class Meta():
    model=music_db
    fields=["title","ascap_id","ascap_pub","ascap_ipi"]

class bmiform(forms.ModelForm):
  class Meta():
    model=music_db
    fields=["title","bmi_id","bmi_pub"]

class gmrform(forms.ModelForm):
  class Meta():
    model=music_db
    fields=["title","gmr_id","gmr_pub","gmr_ipi"]


class searchform(forms.ModelForm):
  class Meta():
    model=music_db
    fields=["title"]