# Generated by Django 4.2.5 on 2023-09-22 12:58

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0014_alter_client_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='birthday',
            field=models.DateField(validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date(2005, 9, 22), message='Регистрация доступна с 18 лет')], verbose_name='Дата рождения'),
        ),
    ]