# Generated by Django 2.2 on 2020-02-04 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingCart', '0002_auto_20200204_0911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopping_cart',
            name='category',
        ),
    ]
