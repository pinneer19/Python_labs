from django.db import models


class ServiceCategory(models.Model):
    name = models.CharField('Категория', max_length=100)

    class Meta:
        verbose_name = 'Категория услуги'
        verbose_name_plural = 'Категории услуг'

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField('Название', max_length=100)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, verbose_name='Категория услуги')
    price = models.FloatField('Стоимость (BYN)')

    class Meta:
        verbose_name = 'услугу'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name
