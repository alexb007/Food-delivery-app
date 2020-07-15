# Generated by Django 3.0.8 on 2020-07-08 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20200708_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='background',
            field=models.ImageField(default='restaurants/noimage.png', upload_to='restaurants/'),
        ),
        migrations.AddField(
            model_name='restauranttype',
            name='icon',
            field=models.ImageField(default='restaurants/noimage.png', upload_to='restaurants/'),
        ),
    ]