# Generated by Django 4.2.5 on 2023-09-14 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Заголовок', max_length=32)),
                ('username', models.CharField(help_text='Логин', max_length=128)),
                ('date', models.DateField(auto_now=True)),
                ('review_text', models.TextField(help_text='Отзыв', max_length=256)),
            ],
        ),
    ]