# Generated by Django 4.1.7 on 2023-04-07 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(default='Nam', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
