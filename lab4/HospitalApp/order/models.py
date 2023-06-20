from django.db import models
from client.models import Client
from service.models import Service
from doctor.models import Doctor


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент', related_name='client')
    date = models.DateField(verbose_name='Дата')

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ клиента {self.client}'


class OrderService(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Услуга')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='Врач', related_name='order_doctor')
    date = models.DateField(verbose_name='Дата')

    class Meta:
        verbose_name = 'заказ услуги к врачу'
        verbose_name_plural = 'Заказы услуг к врачу'

    def __str__(self):
        return f'Заказ услуги {self.service} к врачу {self.doctor}'
