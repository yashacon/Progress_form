# Generated by Django 2.2.4 on 2020-04-19 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='TL',
        ),
        migrations.RemoveField(
            model_name='report',
            name='reports',
        ),
    ]
