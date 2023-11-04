from django import forms
from .models import Message


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input-group'
            }),
            'email': forms.TextInput(attrs={
                'class': 'input-group'
            }),
            'title': forms.TextInput(attrs={
                'class': 'input-group'
            }),
            'body': forms.Textarea(attrs={
                'class': 'input-group'
            })

        }
