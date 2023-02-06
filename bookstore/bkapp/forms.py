from django import forms
from django.db import models


from bkapp.models import Book
from django import  forms


class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['name','img','desc','author']
