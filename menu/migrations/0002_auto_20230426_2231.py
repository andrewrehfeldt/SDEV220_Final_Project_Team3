# Generated by Django 3.2.18 on 2023-04-27 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='dishDescr',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='menu',
            name='dishName',
            field=models.CharField(max_length=200),
        ),
    ]
