# Generated by Django 4.2.1 on 2023-05-14 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0009_alter_doctor_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='user',
        ),
    ]