from django.db import models
from client.models import Client
from service.models import Service
from schedule.models import Schedule
from doctor.models import Doctor


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Услуга')
    # schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, verbose_name='Расписание врача')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='Врач', )

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'Заказы'
