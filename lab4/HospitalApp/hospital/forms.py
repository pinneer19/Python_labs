from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from django.forms import TextInput, PasswordInput, CharField, DateInput, Select


class LoginForm(AuthenticationForm):
    username = CharField(widget=TextInput(attrs={
        'class': 'w-full py-4 px-6 rounded-xl',
        'placeholder': 'Логин'
    }))
    password = CharField(widget=PasswordInput(attrs={
        'class': 'w-full py-4 px-6 rounded-xl',
        'placeholder': 'Пароль'
    }))
