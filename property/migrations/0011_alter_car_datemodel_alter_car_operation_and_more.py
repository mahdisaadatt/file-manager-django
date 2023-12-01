# Generated by Django 4.2.6 on 2023-11-30 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_carattributes_homeattributes_home_attributes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='dateModel',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='operation',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='constructedDate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='home',
            name='meterage',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='home',
            name='mortgage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='pricePerMeter',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='rent',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='rooms',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='other',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
