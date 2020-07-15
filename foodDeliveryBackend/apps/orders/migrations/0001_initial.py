# Generated by Django 3.0.8 on 2020-07-15 20:38

from django.db import migrations, models
import django.db.models.deletion
import django_fsm


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('foods', '0007_auto_20200715_0232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('phone', models.CharField(max_length=13, verbose_name='Phone number')),
                ('contact_name', models.CharField(max_length=100, verbose_name='Contact name')),
                ('comment', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Comment')),
                ('delivery_type', models.CharField(choices=[('deliver', 'Delivery'), ('self', 'Self pick')], default='deliver', max_length=16, verbose_name='Delivery type')),
                ('status', django_fsm.FSMField(choices=[('draft', 'draft'), ('submitted', 'submitted'), ('canceled', 'canceled'), ('inprogress', 'inprogress'), ('ready', 'ready'), ('onroad', 'onroad'), ('delivered', 'delivered'), ('completed', 'completed'), ('payed', 'payed'), ('commented', 'commented')], default='submitted', max_length=50)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(verbose_name='Amount')),
                ('comment', models.CharField(max_length=300)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='orders.Order', verbose_name='Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_products', to='foods.Food', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Order Product',
                'verbose_name_plural': 'Order Products',
            },
        ),
    ]