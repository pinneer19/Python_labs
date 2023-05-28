from django.forms import ModelForm, TextInput, PasswordInput, Select, DateInput, inlineformset_factory
from .models import Order, OrderService


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('client', 'date')

        widgets = {
            'client': Select(attrs={
                'class': 'w-full py-4 px-6 rounded-xl',
                'placeholder': 'Клиент'
            }),
            "date": DateInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl',
                'placeholder': 'Дата заказа'
            }),
        }


class OrderServiceForm(ModelForm):
    class Meta:
        model = OrderService
        fields = ('service', 'doctor', 'date')

        widgets = {
            "service": Select(attrs={
                'class': 'w-full py-4 px-6 rounded-xl',
                'placeholder': 'Услуга'
            }),
            "doctor": Select(attrs={
                'class': 'w-full py-4 px-6 rounded-xl',
                'placeholder': 'Врач'
            }),
            "date": DateInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl',
                'placeholder': 'Дата посещения'
            })
        }
