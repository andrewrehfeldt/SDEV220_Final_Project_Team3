# Generated by Django 3.2.18 on 2023-05-02 04:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0010_alter_customerorder_orderdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorder',
            name='orderDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 2, 0, 22, 15, 99202)),
        ),
    ]
