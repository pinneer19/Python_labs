from django.db import models
from doctor.models import Doctor
from client.models import Client
from service.models import Service


class Visit(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='Врач')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    diagnosis = models.CharField('Диагноз', max_length=50, default='')
    visit_date = models.DateTimeField(verbose_name='Дата посещения')
    service = models.ForeignKey(Service, null=True, on_delete=models.CASCADE, verbose_name='Предоставляемая услуга')

    class Meta:
        verbose_name = 'посещение'
        verbose_name_plural = 'Посещения'

    def __str__(self):
        return f'Посещение врача'
