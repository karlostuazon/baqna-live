# Generated by Django 3.1.7 on 2021-12-02 19:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0055_auto_20211203_0252'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='date_created',
            field=models.DateField(default=datetime.date(2021, 12, 3), null=True),
        ),
    ]
