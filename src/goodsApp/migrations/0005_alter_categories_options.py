# Generated by Django 4.2.7 on 2024-11-11 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodsApp', '0004_alter_categories_name_alter_categories_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Категорию', 'verbose_name_plural': 'Категории'},
        ),
    ]
