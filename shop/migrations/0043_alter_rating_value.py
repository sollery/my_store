# Generated by Django 4.0.4 on 2022-11-19 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0042_messagefromuser_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='value',
            field=models.SmallIntegerField(default=0),
        ),
    ]
