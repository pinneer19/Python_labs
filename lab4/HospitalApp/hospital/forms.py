from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, EmailInput, PasswordInput, CharField
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        widgets = {
            "username": TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl',
                'placeholder': 'Your username'
            }),
            "email": EmailInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl',
                'placeholder': 'Your email'
            })
        }
    password1 = CharField(widget=PasswordInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl',
                'placeholder': 'Your password'
            }))
    password2 = CharField(widget=PasswordInput(attrs={
        'class': 'w-full py-4 px-6 rounded-xl',
        'placeholder': 'Repeat password'
    }))
