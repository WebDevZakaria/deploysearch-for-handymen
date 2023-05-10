from django import forms
from django.forms import ModelForm
from .models import Account,Message


class Registerform(ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(attrs={

        'placeholder': 'Enter Your Password'

    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={

        'placeholder': 'Confirm  Your Password'

    }))

    class Meta:
        model = Account

        fields = ['first_name', 'last_name',

                  'email', 'phone_number', 'wilaya', 'profile_image', 'is_servicecreator', 'password']


def clean(self):

    cleaned_data = super(Registerform, self).clean()

    password = cleaned_data.get('password')

    confirm_password = cleaned_data.get('confirm_password')

    if password != confirm_password:

        raise forms.ValidationError("password not the some! ")


def __init__(self, *args, **kwargs):

    super(Registerform, self).__init__(*args, **kwargs)
    self.fields['first_name'].widget.attrs['placeholder'] = 'Enter your first name'

    for field in self.fields:
        self.fields[field].widget.attrs['class'] = 'form-control'





class formmessage(ModelForm):
    class Meta:
        model = Message

        fields = ['subject', 'body']
