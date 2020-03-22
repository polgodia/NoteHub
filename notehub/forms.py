from django import forms
from notehub import models

class LoginForm(forms.Form):
    DNI = forms.CharField(max_length=20, required=True)
    degree = forms.CharField(max_length=50, required=True)
    starting_date = forms.DateField(required=True)
