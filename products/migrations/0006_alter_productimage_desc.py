# Generated by Django 4.1.7 on 2023-05-05 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_productdetail_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='desc',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
