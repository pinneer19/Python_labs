# Generated by Django 4.2.1 on 2023-05-27 08:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_client_alter_orderservice_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderservice',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата'),
            preserve_default=False,
        ),
    ]
