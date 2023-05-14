from django.db import models
from doctor.models import Doctor
from client.models import Client

class Visit(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='Врач')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    visit_date = models.DateField(verbose_name='Дата посещения')
    duration = models.DurationField(blank=True, null=True, verbose_name='Длительность посещения')
    price = models.FloatField(verbose_name='Цена')

    class Meta:
        verbose_name = 'посещение'
        verbose_name_plural = 'Планируемые посещения'

    def __str__(self):
        return f'{self.doctor} appointment with {self.client}'
