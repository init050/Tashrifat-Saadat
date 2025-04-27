from django import forms
from .models import Contact

class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-white/50 backdrop-blur-sm border-0 rounded-xl px-6 py-4 text-gray-700 shadow-sm focus:ring-2 focus:ring-purple-500 focus:bg-white transition-all duration-300',
                'placeholder': 'نام و نام خانوادگی خود را وارد کنید',
                'autocomplete': 'name',
                'style': 'font-family: Vazirmatn, sans-serif;'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full bg-white/50 backdrop-blur-sm border-0 rounded-xl px-6 py-4 text-gray-700 shadow-sm focus:ring-2 focus:ring-purple-500 focus:bg-white transition-all duration-300',
                'placeholder': 'آدرس ایمیل خود را وارد کنید',
                'autocomplete': 'email',
                'style': 'font-family: Vazirmatn, sans-serif;'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'w-full bg-white/50 backdrop-blur-sm border-0 rounded-xl px-6 py-4 text-gray-700 shadow-sm focus:ring-2 focus:ring-purple-500 focus:bg-white transition-all duration-300',
                'placeholder': 'موضوع پیام خود را وارد کنید',
                'style': 'font-family: Vazirmatn, sans-serif;'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full bg-white/50 backdrop-blur-sm border-0 rounded-xl px-6 py-4 text-gray-700 shadow-sm focus:ring-2 focus:ring-purple-500 focus:bg-white transition-all duration-300',
                'rows': 5,
                'id': 'message',
                'placeholder': 'پیام خود را اینجا بنویسید...',
                'style': 'font-family: Vazirmatn, sans-serif; resize: vertical; min-height: 150px;'
            })
        }

        labels = {
            'name': 'نام و نام خانوادگی',
            'email': 'ایمیل',
            'subject': 'موضوع',
            'message': 'پیام'
        }

        error_messages = {
            'name': {
                'required': 'لطفا نام و نام خانوادگی خود را وارد کنید'
            },
            'email': {
                'required': 'لطفا ایمیل خود را وارد کنید',
                'invalid': 'لطفا یک ایمیل معتبر وارد کنید'
            },
            'subject': {
                'required': 'لطفا موضوع پیام را وارد کنید'
            },
            'message': {
                'required': 'لطفا پیام خود را وارد کنید'
            }
        }