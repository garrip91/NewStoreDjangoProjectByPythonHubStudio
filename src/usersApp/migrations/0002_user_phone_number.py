# Generated by Django 5.1.3 on 2024-12-11 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]