from django import forms
from django.forms import ModelForm
from .models import *

class LoginForm(ModelForm):
    class Meta:
        model=Register
        fields=['username','password']
        help_texts = {
            'username' : None
        }
