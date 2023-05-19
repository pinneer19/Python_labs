from django.db import models
from doctor.models import Doctor


class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField('Дата')
    start_time = models.TimeField()
    end_time = models.TimeField()
    planned_visits = models.ManyToManyField(PlannedVisit, blank=True)

    class Meta:
        verbose_name = 'Расписание приемов'
        verbose_name_plural = 'Расписания приемов'
