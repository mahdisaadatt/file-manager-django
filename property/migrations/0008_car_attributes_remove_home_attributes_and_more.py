# Generated by Django 4.2.6 on 2023-11-30 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_alter_home_attributes'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='attributes',
            field=models.ManyToManyField(blank=True, to='property.car'),
        ),
        migrations.RemoveField(
            model_name='home',
            name='attributes',
        ),
        migrations.AddField(
            model_name='home',
            name='attributes',
            field=models.ManyToManyField(blank=True, to='property.home'),
        ),
    ]
