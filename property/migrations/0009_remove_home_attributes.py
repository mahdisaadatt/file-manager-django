# Generated by Django 4.2.6 on 2023-11-30 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_car_attributes_remove_home_attributes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='attributes',
        ),
    ]