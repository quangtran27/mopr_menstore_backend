# Generated by Django 4.2.1 on 2023-05-11 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('images', models.ImageField(upload_to='images/banners/%Y/%m/%D/')),
            ],
        ),
    ]
