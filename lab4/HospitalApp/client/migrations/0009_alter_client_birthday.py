# Generated by Django 4.2.1 on 2023-05-27 08:53

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_alter_client_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='birthday',
            field=models.DateField(validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date(2005, 5, 27))], verbose_name='Дата рождения'),
        ),
    ]
