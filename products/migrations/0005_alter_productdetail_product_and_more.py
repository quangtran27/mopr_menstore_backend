# Generated by Django 4.1.7 on 2023-05-05 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_name_alter_productdetail_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetail',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
