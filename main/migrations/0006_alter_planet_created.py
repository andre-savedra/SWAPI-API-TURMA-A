# Generated by Django 4.2.4 on 2023-09-27 22:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_planet_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planet',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 27, 22, 25, 45, 420909, tzinfo=datetime.timezone.utc)),
        ),
    ]