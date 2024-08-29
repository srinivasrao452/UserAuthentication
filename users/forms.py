
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

## This is a comment line from server side added

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

