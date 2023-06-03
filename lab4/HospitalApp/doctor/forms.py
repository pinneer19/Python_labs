from django.forms import ModelForm, TextInput, Select, PasswordInput, ModelMultipleChoiceField, SelectMultiple

from .models import Doctor, Specialization


class DoctorSignUpForm(ModelForm):
    class Meta:
        model = Doctor

        fields = ('first_name', 'last_name', 'middle_name', 'department', 'specialization', 'login', 'password')

        widgets = {
            "first_name": TextInput(attrs={
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
            # "specialization": Select(attrs={
            #     'class': 'w-full py-4 px-6 rounded-xl bg-white',
            #     'data-placeholder': 'Специализация'
            # }),
            "login": TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl',
                'placeholder': 'Логин'
            }),
            "password": PasswordInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl',
                'placeholder': 'Пароль'
            })
        }
    specialization = ModelMultipleChoiceField(
        queryset=Specialization.objects.all(),
        widget=SelectMultiple(attrs={
            'class': 'w-full py-4 px-6 rounded-xl'
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].empty_label = 'Отделение'
        self.fields['specialization'].empty_label = 'Специализация'
