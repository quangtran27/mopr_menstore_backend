# Generated by Django 4.1.7 on 2023-04-06 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='product_detail',
            new_name='product',
        ),
    ]
