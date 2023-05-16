from django.db import models
from doctor.models import Doctor



class AppointmentSchedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        verbose_name = 'Расписание приемов'
        verbose_name_plural = 'Расписания приемов'
