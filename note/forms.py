from django import forms
from .models import *

class NoteForms(forms.ModelForm):

    class Meta:
        model = Note
        fields = ["contents","notetype"]
        exclude = [""]