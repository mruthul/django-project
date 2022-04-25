from django import forms
from app1.models import Image, Signup

class Loginform(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8)
    class Meta():
        model=Signup
        fields=('Email','Password')



class Editform(forms.ModelForm):
    class Meta():
        model=Signup
        fields=('Name','Email')        

class Changepassword(forms.Form):
    Old_Password=forms.CharField(widget=forms.PasswordInput,max_length=8)
    New_Password=forms.CharField(widget=forms.PasswordInput,max_length=8)
    Confirm_Password=forms.CharField(widget=forms.PasswordInput,max_length=8)

  