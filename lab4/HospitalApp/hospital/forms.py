import re

from django.forms import ModelForm, ValidationError, inlineformset_factory
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import TextInput, EmailInput, PasswordInput, CharField, DateInput, ModelChoiceField, Select
from django.contrib.auth.models import User

from client.models import Client, Passport
from doctor.models import Doctor, Department, Specialization


class PassportForm(ModelForm):
    class Meta:
        model = Passport
        fields = ('serial', 'number')

        widgets = {
            'serial': TextInput(attrs={
                'class': 'py-4 px-4 rounded-xl',
                'placeholder': 'Серия паспорта'
            }),
            "number": TextInput(attrs={
                'class': 'w-full py-4 px-4 rounded-xl',
                'placeholder': 'Номер паспорта'
            })
        }


class LoginForm(AuthenticationForm):
    username = CharField(widget=TextInput(attrs={
        'class': 'w-full py-4 px-6 rounded-xl',
        'placeholder': 'Логин'
    }))
    password = CharField(widget=PasswordInput(attrs={
        'class': 'w-full py-4 px-6 rounded-xl',
        'placeholder': 'Пароль'
    }))


class ClientSignUpForm(ModelForm):
    passport = PassportForm()

    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'middle_name', 'birthday', 'address', 'phone', 'password')

        widgets = {
            'first_name': TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl',
                'placeholder': 'Имя'
            }),
            "last_name": TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl',
                'placeholder': 'Фамилия'
            }),
            "middle_name": TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl',
                'placeholder': 'Отчество'
            }),
            "birthday": DateInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl',
                'placeholder': 'Дата рождения'
            }),
            "address": TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl',
                'placeholder': 'Адрес'
            }),
            "phone": TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl',
                'placeholder': 'Номер телефона'
            }),
            "password": PasswordInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl',
                'placeholder': 'Пароль'
            })
        }


class DoctorSignUpForm(ModelForm):

    class Meta:
        model = Doctor

        fields = ('first_name', 'last_name', 'middle_name', 'department', 'specialization', 'login', 'password')

        widgets = {
            'first_name': TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl',
                'placeholder': 'Имя'
            }),
            "last_name": TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl',
                'placeholder': 'Фамилия'
            }),
            "middle_name": TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl',
                'placeholder': 'Отчество'
            }),
            "department": Select(attrs={
                'class': 'w-full py-4 px-6 rounded-xl bg-white',
                'placeholder': 'Отделение'
            }),
            "specialization": Select(attrs={
                'class': 'w-full py-4 px-6 rounded-xl bg-white',
                'data-placeholder': 'Специализация'
            }),
            'login': TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl',
                'placeholder': 'Логин'
            }),
            'password': PasswordInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl',
                'placeholder': 'Пароль'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.fields['department'].empty_label = 'Отделение'
        self.fields['specialization'].empty_label = 'Специализация'
