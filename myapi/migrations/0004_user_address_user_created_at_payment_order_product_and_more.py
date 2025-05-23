# Generated by Django 5.1.6 on 2025-05-14 11:31

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_alter_user_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('payment_method', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='myapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('order_date', models.DateField(auto_now_add=True)),
                ('total_price', models.FloatField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='myapi.user')),
                ('payment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='myapi.payment')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('sku', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('price', models.IntegerField(default=0)),
                ('stock', models.IntegerField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='myapi.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order_item',
            fields=[
                ('order_item_id', models.IntegerField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='myapi.order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='myapi.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.IntegerField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='myapi.user')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_item', to='myapi.product')),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('shipment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('shipment_date', models.DateField(default=datetime.datetime.today)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('zip_code', models.IntegerField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='myapi.user')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='Shipment_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipment', to='myapi.shipment'),
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('wishlist_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist_item', to='myapi.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist', to='myapi.user')),
            ],
        ),
    ]
