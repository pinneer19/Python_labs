# Generated by Django 4.2.1 on 2023-05-27 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_order_date_alter_orderservice_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
    ]
