# Generated by Django 4.1.10 on 2024-08-23 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scraping", "0003_alter_product_last_7_day_sale"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="last_7_day_sale",
            field=models.TextField(default="0"),
        ),
    ]
