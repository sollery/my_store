# Generated by Django 4.0.4 on 2022-08-29 22:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0015_alter_discount_product_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount_product',
            name='end',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='discount_product',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='Review_answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(verbose_name='Ответ на комментарий')),
                ('active', models.BooleanField(default=True)),
                ('created_rew', models.DateTimeField(auto_now_add=True)),
                ('updated_rew', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_answer', to='shop.product')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_answer', to='shop.review')),
            ],
        ),
    ]
