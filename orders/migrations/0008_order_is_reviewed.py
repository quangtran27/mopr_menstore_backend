# Generated by Django 4.1.7 on 2023-05-05 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_reviewed',
            field=models.BooleanField(default=False),
        ),
    ]
