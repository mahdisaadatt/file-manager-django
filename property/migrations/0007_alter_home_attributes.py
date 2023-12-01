# Generated by Django 4.2.6 on 2023-11-25 17:24

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_alter_home_attributes_alter_home_hometype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='attributes',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('آسانسور', 'آسانسور'), ('پارکینگ', 'پارکینگ'), ('انباری', 'انباری'), ('حیاط', 'حیاط'), ('رو به نما', 'رو به نما'), ('اتاق خواب مستر', 'اتاق خواب مستر')], max_length=60, null=True),
        ),
    ]