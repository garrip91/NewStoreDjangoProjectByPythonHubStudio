# Generated by Django 4.2.7 on 2024-11-13 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodsApp', '0006_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='Скидка'),
        ),
    ]