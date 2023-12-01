# Generated by Django 4.2.6 on 2023-11-30 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_remove_home_attributes'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarAttributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=156)),
            ],
        ),
        migrations.CreateModel(
            name='HomeAttributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=156)),
            ],
        ),
        migrations.AddField(
            model_name='home',
            name='attributes',
            field=models.ManyToManyField(blank=True, null=True, related_name='attributes', to='property.homeattributes'),
        ),
        migrations.AlterField(
            model_name='car',
            name='attributes',
            field=models.ManyToManyField(blank=True, null=True, related_name='attributes', to='property.carattributes'),
        ),
    ]