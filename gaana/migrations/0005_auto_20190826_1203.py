# Generated by Django 2.2.3 on 2019-08-26 06:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gaana', '0004_auto_20190823_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='DOB',
            field=models.DateField(default=datetime.datetime(2019, 8, 26, 12, 3, 49, 897686)),
        ),
        migrations.CreateModel(
            name='ShipPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('carplates', models.CharField(max_length=20)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]