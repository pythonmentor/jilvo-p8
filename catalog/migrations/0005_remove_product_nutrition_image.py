# Generated by Django 3.0.8 on 2020-09-22 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_product_nutrition_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='nutrition_image',
        ),
    ]
