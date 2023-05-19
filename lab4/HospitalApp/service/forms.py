from django.forms import ModelForm, TextInput, Select, NumberInput
from .models import Service


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ('name', 'category', 'price')
        widgets = {
            'category': Select(attrs={'class': 'ml-2 my-4 border-2 w-1/2 py-4 px-6 rounded-xl bg-white',
                                      'data-placeholder': 'Категория'}),
            "name": TextInput(attrs={
                'class': 'ml-2 my-4 border-2 w-1/2 py-4 px-6 rounded-xl',
                'placeholder': 'Название'
            }),
            "price": NumberInput(attrs={
                'class': 'ml-2 my-4 border-2 w-1/2 py-4 px-6 rounded-xl',
                'placeholder': 'Стоимость'
            })
        }