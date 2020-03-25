from datetime import datetime
from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError

from notehub.models import Student


class SignupForm(ModelForm):
    username = forms.CharField(max_length=20)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, strip=False)
    password2 = forms.CharField(label="Password2", widget=forms.PasswordInput, strip=False)
    DNI = forms.CharField(max_length=20, required=True)
    degree = forms.CharField(max_length=50, required=True)
    starting_date = forms.DateField(required=True)

    class Meta:
        model = Student
        fields = ['username', 'password1', 'password2', 'DNI', 'degree', 'starting_date']

    def clean_renewal_date(self):
        start = self.cleaned_data['starting_date']
        passw = self.cleaned_data['password1']
        passw2 = self.cleaned_data['password2']

        # Check date is not in past.
        if start < datetime.date.today():
            raise ValidationError('Invalid date')

        if passw != passw2:
            raise ValidationError('Passwords do not coincide')
