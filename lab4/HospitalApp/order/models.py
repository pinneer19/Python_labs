from django.db import models
from client.models import Client
from service.models import Service


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    services = models.ManyToManyField(Service, verbose_name='Услуги')
    total_price = models.FloatField('Общая стоимость')

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'Заказы'
