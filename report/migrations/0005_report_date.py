# Generated by Django 2.2.4 on 2020-04-19 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_auto_20200419_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Date'),
        ),
    ]
