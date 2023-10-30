from django import forms

from .models import *

class RejaForm(forms.ModelForm):
    class Meta:
        model = Malumot
        fields = "__all__"

