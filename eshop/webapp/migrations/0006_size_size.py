# Generated by Django 4.1.1 on 2022-10-22 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_product_minimumprice_product_minimumprice_currency_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='size',
            name='size',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
