# Generated by Django 3.2.18 on 2023-03-29 21:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menuNbr', models.IntegerField()),
                ('dishName', models.TextField()),
                ('dishDescr', models.CharField(max_length=200)),
                ('itemPrice', models.FloatField()),
                ('servSize', models.IntegerField()),
                ('customerOpts', models.CharField(max_length=50)),
                ('effectiveDate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]