# Generated by Django 4.2.1 on 2023-05-12 17:58

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=2, validators=[django.core.validators.RegexValidator(message='Введена несуществующая серия паспорта', regex='^(АВ|ВМ|НВ|КН|МР|МС|КВ|РР|SP|DP)$')], verbose_name='Серия паспорта')),
                ('number', models.CharField(max_length=25, validators=[django.core.validators.RegexValidator(message='Введен некорректный номер паспорта', regex='^\\d{7}$')], verbose_name='Номер паспорта')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=25, verbose_name='Фамилия')),
                ('middle_name', models.CharField(max_length=25, verbose_name='Отчество')),
                ('birthday', models.DateField(validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date(2005, 5, 12))], verbose_name='Дата рождения')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=19, validators=[django.core.validators.RegexValidator(message='Номер телефона должен быть в указанном формате: +375 (XX) XXX-XX-XX', regex='^\\+375 \\(\\d{2}\\) \\d{3}-\\d{2}-\\d{2}$')], verbose_name='Номер телефона')),
                ('passport', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='client.passport', verbose_name='Серия/Номер паспорта')),
            ],
            options={
                'verbose_name': 'клиента',
                'verbose_name_plural': 'Клиенты',
            },
        ),
    ]
