# Generated by Django 4.2.1 on 2023-05-16 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0011_doctor_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialization',
            name='department',
            field=models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, to='doctor.department', verbose_name='Отделение'),
        ),
    ]