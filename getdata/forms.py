from django import forms
from .models import *

class NoteForms(forms.ModelForm):

    class Meta:
        model = Notes
        fields = ["contents","notetype"]
        exclude = [""]