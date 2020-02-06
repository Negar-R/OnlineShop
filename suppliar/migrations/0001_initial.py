# Generated by Django 2.2 on 2020-02-06 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shoppingCart', '0003_remove_shopping_cart_category'),
        ('userProfile', '0003_delete_userprofileadvance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suppliar_Check_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('ready', 'Ready to send'), ('on_process', 'On Process')], max_length=50)),
                ('factor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppingCart.Shopping_Cart')),
                ('reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userProfile.UserProfile')),
            ],
        ),
    ]
