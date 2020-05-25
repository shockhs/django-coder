from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TextForm(forms.Form):
    textEntered = forms.CharField(max_length=1000),
    textEncoded = forms.CharField(max_length=1000),
    rails = forms.IntegerField(),
    username = forms.CharField(max_length=100)