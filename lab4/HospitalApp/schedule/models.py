from django.db import models
from doctor.models import Doctor


class Schedule(models.Model):
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    # date = models.DateField('Дата

    class Meta:
        verbose_name = 'Расписание приемов'
        verbose_name_plural = 'Расписания приемов'
