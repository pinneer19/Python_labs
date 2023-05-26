# Generated by Django 4.2.1 on 2023-05-25 14:42

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_alter_client_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='birthday',
            field=models.DateField(validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date(2005, 5, 25))], verbose_name='Дата рождения'),
        ),
    ]
