from django.forms import ModelForm, TextInput, DateInput, PasswordInput
from .models import Passport, Client


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
