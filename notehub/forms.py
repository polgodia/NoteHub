from datetime import datetime
from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from notehub.models import Student, Document, Exam, Exercice, Note


class SignupForm(ModelForm):
    username = forms.CharField(max_length=20, required=True)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, strip=False, required=True)
    password2 = forms.CharField(label="Password2", widget=forms.PasswordInput, strip=False, required=True)
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


class AddExamForm(ModelForm):
    PARCIAL_NUMBER = ((1, 'First'), (2, 'Second'))
    name = forms.CharField(max_length=50, required=True)
    content = forms.CharField(max_length=2000, required=True)
    degree = forms.CharField(max_length=50, required=True)
    subject = forms.CharField(max_length=50, required=True)
    date = forms.DateField()
    parcial = forms.CheckboxSelectMultiple(choices=PARCIAL_NUMBER)
    solved = forms.BooleanField(required=True)

    class Meta:
        model = Exam
        fields = ['name', 'content', 'degree', 'subject', 'date', 'parcial', 'solved']


class AddExerciseForm(ModelForm):
    name = forms.CharField(max_length=50, required=True)
    content = forms.CharField(max_length=2000, required=True)
    degree = forms.CharField(max_length=50, required=True)
    subject = forms.CharField(max_length=50, required=True)
    unit = forms.IntegerField(required=True)
    corrected = forms.BooleanField(required=True)

    class Meta:
        model = Exercice
        fields = ['name', 'content', 'degree', 'subject', 'unit', 'corrected']


class AddNoteForm(ModelForm):
    name = forms.CharField(max_length=50, required=True)
    content = forms.CharField(max_length=2000, required=True)
    degree = forms.CharField(max_length=50, required=True)
    subject = forms.CharField(max_length=50, required=True)
    unit = forms.IntegerField()
    date = forms.DateField()

    class Meta:
        model = Note
        fields = ['name', 'content', 'degree', 'subject', 'unit', 'date']
