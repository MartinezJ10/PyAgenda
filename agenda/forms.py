from django import forms

from .models import Agenda


class CreateContact(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = "__all__"
