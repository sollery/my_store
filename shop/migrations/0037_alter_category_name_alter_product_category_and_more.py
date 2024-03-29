# Generated by Django 4.0.4 on 2022-10-15 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0036_remove_product_count_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
    ]
