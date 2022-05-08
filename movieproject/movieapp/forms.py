from .models import Movie
from django import forms
from django.forms import ModelForm

class MovieForms(ModelForm):
   class Meta:
    model =Movie
    fields=['name','desc','year','img']
