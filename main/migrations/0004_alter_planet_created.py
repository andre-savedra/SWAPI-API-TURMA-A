# Generated by Django 4.2.4 on 2023-08-31 00:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_planet_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planet',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 31, 0, 59, 26, 198379, tzinfo=datetime.timezone.utc)),
        ),
    ]
