# Generated by Django 4.2.6 on 2023-11-18 08:15

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_alter_car_address_alter_car_cover_alter_home_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='attributes',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('آسانسور', 'آسانسور'), ('پارکینگ', 'پارکینگ'), ('انباری', 'انباری'), ('اتاق خواب مستر', 'اتاق خواب مستر'), ('حیاط', 'حیاط')], max_length=60),
        ),
        migrations.AlterField(
            model_name='home',
            name='homeType',
            field=models.CharField(blank=True, choices=[('فروش', 'فروش'), ('رهن و اجاره', 'رهن و اجاره')], max_length=60, null=True),
        ),
    ]
