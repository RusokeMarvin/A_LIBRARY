from dataclasses import fields
from django import forms
from django import forms
from .models import Siteuser
from django import forms
from.models import Book
from django.forms import ModelForm


class BookForm(ModelForm):
    class meta:
        model=Book
        fields='__all__'


class Loginform(forms.Form):
    username= forms.CharField(max_length= 25,label="Enter username")
    password= forms.CharField(max_length= 30, label='Password', widget=forms.PasswordInput)

GENDER_CHOICES= [
    ('First choice', 'I am...'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ]

college_choices= [
    ('cedat', 'cedat'),
    ('cocis', 'cocis'),
    ('combas', 'combas'),
    ('elais', 'elais'),
    ]

YEARS= [x for x in range(1920,2022)]


class Signupform(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    birth_date= forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    gender= forms.CharField(widget=forms.Select(choices=GENDER_CHOICES))
    college= forms.CharField(widget=forms.Select(choices=college_choices))
    registration_no=forms.CharField()

    class Meta:
        model= Siteuser
        fields= ["firstname", "lastname",
                 "username", "password1",
                 "password2",
                 "birth_date",
                 "gender",
                 "email", "phone", 
                 "college",
                 "registration_no"]