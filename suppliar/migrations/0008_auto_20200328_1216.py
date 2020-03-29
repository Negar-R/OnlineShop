# Generated by Django 2.2 on 2020-03-28 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suppliar', '0007_auto_20200327_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='suppliar_check_order',
            name='address',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='suppliar_check_order',
            name='phone',
            field=models.CharField(default='', max_length=11),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='suppliar_check_order',
            name='reciever',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]