# Generated by Django 2.2.3 on 2019-08-23 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaana', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='DOB',
            field=models.DateField(default=datetime.datetime(2019, 8, 23, 23, 6, 25, 520574)),
        ),
    ]
