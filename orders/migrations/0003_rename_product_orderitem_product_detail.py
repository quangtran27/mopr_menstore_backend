# Generated by Django 4.1.7 on 2023-04-06 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_rename_product_detail_orderitem_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='product',
            new_name='product_detail',
        ),
    ]
