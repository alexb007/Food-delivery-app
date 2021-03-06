# Generated by Django 3.0.8 on 2020-07-15 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0004_auto_20200708_0046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food',
            options={'verbose_name': 'Food Category', 'verbose_name_plural': 'Food Categories'},
        ),
        migrations.AlterModelOptions(
            name='foodcategory',
            options={'verbose_name': 'Food Category', 'verbose_name_plural': 'Food Categories'},
        ),
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]
