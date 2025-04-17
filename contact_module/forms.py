from django import forms
from .models import Contact

class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model =Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 5,
                'id': 'message'
            })
        }

        labels = {
            'name': 'Your Name and your last name',
            'email': 'Your email'
        }

        error_messages ={
            'name':{
                'required': 'Please enter your name and your last name'
            }
        }