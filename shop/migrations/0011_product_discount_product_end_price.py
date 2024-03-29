# Generated by Django 4.0.4 on 2022-08-28 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_rating_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(blank=True, default=0, verbose_name='Скидка в процентах'),
        ),
        migrations.AddField(
            model_name='product',
            name='end_price',
            field=models.IntegerField(default=0, verbose_name='Итоговая цена'),
        ),
    ]
