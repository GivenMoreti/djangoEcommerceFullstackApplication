# Generated by Django 4.1.3 on 2022-11-26 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_rename_date_product_date_of_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_of_stock',
            field=models.DateField(auto_now_add=True),
        ),
    ]
