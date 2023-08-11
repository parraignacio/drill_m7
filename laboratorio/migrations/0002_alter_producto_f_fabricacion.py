# Generated by Django 4.1.1 on 2023-08-09 20:17

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='f_fabricacion',
            field=models.DateField(default=datetime.date(2015, 1, 1), validators=[django.core.validators.MinValueValidator(datetime.date(2015, 1, 1))]),
        ),
    ]
