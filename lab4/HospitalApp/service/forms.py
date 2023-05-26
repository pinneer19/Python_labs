from django.forms import ModelForm, TextInput, Select, NumberInput
from .models import Service


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ('name', 'category', 'price')
        widgets = {
            'category': Select(attrs={'class': 'border-2 w-full py-4 px-6 rounded-xl bg-white',
                                      'data-placeholder': 'Категория'}),
            "name": TextInput(attrs={
                'class': 'border-2 w-full py-4 px-6 rounded-xl',
                'placeholder': 'Название'
            }),
            "price": NumberInput(attrs={
                'class': 'border-2 w-full py-4 px-6 rounded-xl',
                'placeholder': 'Стоимость'
            })
        }