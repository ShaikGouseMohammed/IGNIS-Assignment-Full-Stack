# Generated by Django 4.1.10 on 2024-08-23 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scraping", "0006_alter_product_length_alter_product_pattern_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sku",
            name="color",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="sku",
            name="size",
            field=models.CharField(default="", max_length=200),
        ),
    ]
