# Generated by Django 4.0.4 on 2022-11-22 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0022_order_status_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='nrYzBU', max_length=6, verbose_name='Cекретный ключ'),
        ),
    ]
