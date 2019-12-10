from  .models import Users, Trade, Trade_close
from django import forms
from django.forms import ModelForm, Form


class RegForm(Form):
    login = forms.CharField(required=True, max_length=250)
    password = forms.CharField(required=True, max_length=250)