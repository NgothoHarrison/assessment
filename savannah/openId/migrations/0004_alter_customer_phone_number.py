# Generated by Django 5.1.1 on 2024-09-24 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openId', '0003_alter_customer_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]
