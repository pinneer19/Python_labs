# Generated by Django 4.2.1 on 2023-05-14 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0011_doctor_user'),
        ('client', '0004_client_user_alter_client_birthday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_date', models.DateField()),
                ('duration', models.DurationField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
            ],
            options={
                'verbose_name': 'посещение',
                'verbose_name_plural': 'Планируемые посещения',
            },
        ),
    ]
