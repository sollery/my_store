# Generated by Django 4.0.4 on 2022-11-07 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='jgVTgk', max_length=6, verbose_name='Cекретный ключ'),
        ),
    ]
