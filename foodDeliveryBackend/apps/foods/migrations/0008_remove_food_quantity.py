# Generated by Django 3.0.8 on 2020-07-15 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0007_auto_20200715_0232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='quantity',
        ),
    ]
