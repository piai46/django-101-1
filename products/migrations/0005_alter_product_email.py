# Generated by Django 4.1.7 on 2023-04-01 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
