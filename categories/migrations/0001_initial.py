# Generated by Django 4.1.7 on 2023-04-24 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('desc', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/category/%Y/%m/%D/')),
            ],
        ),
    ]