from django import forms
from django.forms.forms import Form

class name_form(forms.Form):
    your_name=forms.CharField(label="Your Name",max_length=100)