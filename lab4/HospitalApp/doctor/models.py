from django.db import models


class Department(models.Model):
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = 'отделение'
        verbose_name_plural = 'Отделения'

    def __str__(self):
        return self.name


class Specialization(models.Model):
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = 'специализацию'
        verbose_name_plural = 'Специализации'

    def __str__(self):
        return self.name


class Doctor(models.Model):
    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    middle_name = models.CharField('Отчество', max_length=255)
    login = models.CharField('Логин', max_length=25, default='')
    password = models.CharField('Пароль', max_length=25, default='')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='doctors',
                                   verbose_name='Отделение')
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, related_name='doctors',
                                       verbose_name='Специализация')

    class Meta:
        verbose_name = 'врача'
        verbose_name_plural = 'Врачи'

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'
