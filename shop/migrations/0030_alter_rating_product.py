# Generated by Django 4.0.4 on 2022-10-10 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0029_alter_productaccessories_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='shop.product'),
        ),
    ]