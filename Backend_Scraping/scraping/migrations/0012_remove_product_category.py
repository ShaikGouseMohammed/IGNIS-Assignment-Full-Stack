# Generated by Django 4.1.10 on 2024-08-23 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("scraping", "0011_alter_product_fabric_alter_product_length_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="category",
        ),
    ]
