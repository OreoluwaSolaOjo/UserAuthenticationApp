from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        email = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')
