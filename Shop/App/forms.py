from django.forms import TextInput, EmailInput
from .models import Subscribers
from django import forms


class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ['email', 'name']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name',
            }),

            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }),
        }
