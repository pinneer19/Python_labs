from django.forms import ModelForm, TextInput, Select
from django.utils.dateparse import parse_duration

from .models import Visit

class VisitForm(ModelForm):
    class Meta:
        model = Visit

        fields = ('diagnosis',)

        widgets = {
            'diagnosis': TextInput(attrs={
                'class': 'py-4 px-4 rounded-xl w-full',
                'placeholder': 'Диагноз'
            })
        }
