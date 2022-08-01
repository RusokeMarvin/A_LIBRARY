from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from . import models
 
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )    