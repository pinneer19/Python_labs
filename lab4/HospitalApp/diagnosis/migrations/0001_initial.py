# Generated by Django 4.2.1 on 2023-05-12 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('doctor', '0003_alter_department_options_alter_doctor_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Диагноз')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('date', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diagnoses', to='client.client', verbose_name='Клиент')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diagnoses', to='doctor.doctor', verbose_name='Врач')),
            ],
            options={
                'verbose_name': 'диагноз',
                'verbose_name_plural': 'Диагнозы',
            },
        ),
    ]