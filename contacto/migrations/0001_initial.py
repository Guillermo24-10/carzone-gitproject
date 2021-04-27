# Generated by Django 3.0.7 on 2021-04-14 22:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('car_id', models.IntegerField()),
                ('customer_need', models.CharField(max_length=100)),
                ('car_tittle', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('mensaje', models.TextField(blank=True)),
                ('user_id', models.IntegerField(blank=True)),
                ('fecha_creacion', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
