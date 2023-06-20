from django.db import models
from client.models import Client
from doctor.models import Doctor


class Diagnosis(models.Model):
    name = models.CharField('Диагноз', max_length=255)
    description = models.TextField('Описание', blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='diagnoses', verbose_name='Клиент')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='diagnoses', verbose_name='Врач')
    date = models.DateField()

    class Meta:
        verbose_name_plural = 'Диагнозы'
        verbose_name = 'диагноз'

    def __str__(self):
        return self.name
