# Generated by Django 5.2.3 on 2025-06-30 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0005_category_language"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
