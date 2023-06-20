from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator
from datetime import date


class Passport(models.Model):
    serial_validator = RegexValidator(
        regex=r'^(AB|BM|HB|KH|MP|MC|KB|PP|SP|DP)$',
        message='Введена несуществующая серия паспорта'
    )
    serial = models.CharField('Серия паспорта', max_length=2, validators=[serial_validator])

    number_validator = RegexValidator(
        regex=r'^\d{7}$',
        message='Введен некорректный номер паспорта'
    )
    number = models.CharField('Номер паспорта', max_length=25, validators=[number_validator])

    def __str__(self):
        return f'{self.serial}{self.number}'


User = get_user_model()


class Client(models.Model):
    first_name = models.CharField('Имя', max_length=25)
    last_name = models.CharField('Фамилия', max_length=25)
    middle_name = models.CharField('Отчество', max_length=25)
    passport = models.OneToOneField(Passport, on_delete=models.CASCADE, verbose_name='Серия/Номер паспорта')
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    password = models.CharField('Пароль', max_length=25, default='')
    birthday = models.DateField('Дата рождения', validators=[
        MaxValueValidator(limit_value=date.today().replace(year=date.today().year - 18),
                          message='Регистрация доступна с 18 лет')])
    address = models.CharField('Адрес', max_length=255)

    phone_regex = RegexValidator(
        regex=r'^\+375 \(\d{2}\) \d{3}-\d{2}-\d{2}$',
        message='Номер телефона должен быть в указанном формате: +375 (XX) XXX-XX-XX'
    )
    phone = models.CharField('Номер телефона', validators=[phone_regex], max_length=19)

    class Meta:
        verbose_name = 'клиента'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.last_name} {self.first_name[:1]}.{self.middle_name[:1]}.'
