# Generated by Django 3.0.8 on 2020-08-02 16:30

from django.db import migrations, models
import django.db.models.deletion


def rename_model(apps, schema_editor):
    categories = []
    RestaurantType = apps.get_model('restaurants', 'RestaurantType')
    Category = apps.get_model('restaurants', 'RestaurantCategory')
    BusinessType = apps.get_model('restaurants', 'BusinessType')
    restaurant = BusinessType.objects.create(name='Рестораны', order=1)
    shop = BusinessType.objects.create(name='Магазины', order=2)
    for restaurantType in RestaurantType.objects.all():
        categories.append(Category(name=restaurantType.name, icon=restaurantType.icon, business=restaurant))
    Category.objects.bulk_create(categories)


class Migration(migrations.Migration):
    dependencies = [
        ('restaurants', '0004_auto_20200708_0221'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Business Name')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Order in main page')),
            ],
            options={
                'verbose_name': 'Business Type',
                'verbose_name_plural': 'Business Type',
                'ordering': ('order', 'name'),
            },
        ),
        migrations.CreateModel(
            name='RestaurantCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('icon', models.ImageField(default='restaurants/noimage.png', upload_to='restaurants/')),
                ('business',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.BusinessType',
                                   verbose_name='Business')),
            ],
            options={
                'verbose_name': 'Restaurant Type',
                'verbose_name_plural': 'Restaurant Types',
                'ordering': ('name', '-id'),
            },
        ),
        migrations.RunPython(rename_model),
        migrations.AlterField(
            model_name='restaurant',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurants',
                                    to='restaurants.RestaurantCategory', verbose_name='Restaurant Type'),
        ),

        migrations.DeleteModel(
            name='RestaurantType',
        ),
    ]
