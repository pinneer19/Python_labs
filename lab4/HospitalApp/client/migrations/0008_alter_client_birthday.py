# Generated by Django 4.2.1 on 2023-05-26 10:19

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_alter_client_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='birthday',
            field=models.DateField(validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date(2005, 5, 26))], verbose_name='Дата рождения'),
        ),
    ]
