# Generated by Django 4.2.1 on 2023-05-16 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_alter_client_birthday'),
        ('doctor', '0012_specialization_department'),
        ('visit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='price',
        ),
        migrations.AlterField(
            model_name='visit',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor', verbose_name='Врач'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='duration',
            field=models.DurationField(blank=True, null=True, verbose_name='Длительность посещения'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='visit_date',
            field=models.DateField(verbose_name='Дата посещения'),
        ),
    ]
