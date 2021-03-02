# Generated by Django 2.2 on 2021-03-01 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='ItemsPic')),
                ('category', models.CharField(choices=[('Digital_Product', 'Digital_Product'), ('Home_Appliance', 'Home_Appliance'), ('Educational', 'Educational')], max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('slug', models.SlugField(null=True, unique=True)),
                ('created_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DigitalProduct',
            fields=[
                ('baseitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.BaseItem')),
                ('color', models.CharField(choices=[('black', 'black'), ('white', 'white'), ('silver', 'silver'), ('blue', 'blue'), ('red', 'red'), ('green', 'green'), ('yellow', 'yellow')], max_length=100)),
                ('ram_Gig', models.SmallIntegerField()),
            ],
            bases=('content.baseitem',),
        ),
        migrations.CreateModel(
            name='Educational',
            fields=[
                ('baseitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.BaseItem')),
                ('recommendede_ages', models.CharField(max_length=200)),
            ],
            bases=('content.baseitem',),
        ),
        migrations.CreateModel(
            name='HomeAppliance',
            fields=[
                ('baseitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.BaseItem')),
                ('color', models.CharField(choices=[('black', 'black'), ('white', 'white'), ('silver', 'silver'), ('blue', 'blue'), ('red', 'red'), ('green', 'green'), ('yellow', 'yellow')], max_length=60, null=True)),
                ('weight', models.SmallIntegerField(default=0, null=True)),
            ],
            bases=('content.baseitem',),
        ),
        migrations.CreateModel(
            name='TopProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_detail', models.URLField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.BaseItem')),
            ],
        ),
        migrations.CreateModel(
            name='AmazingOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_detail', models.URLField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.BaseItem')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('educational_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.Educational')),
                ('author', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('language', models.CharField(choices=[('persian', 'persian'), ('english', 'englih')], max_length=50)),
            ],
            bases=('content.educational',),
        ),
        migrations.CreateModel(
            name='Laptob',
            fields=[
                ('digitalproduct_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.DigitalProduct')),
                ('screen_size', models.CharField(max_length=100)),
                ('touch_screen_display', models.BooleanField()),
                ('graphics_card', models.BooleanField()),
            ],
            bases=('content.digitalproduct',),
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('digitalproduct_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.DigitalProduct')),
                ('operation_system', models.CharField(choices=[('android', 'Android'), ('ios', 'IOS')], max_length=10)),
                ('display_resolution', models.CharField(max_length=100)),
                ('sim_card', models.CharField(choices=[('S', 'Standard'), ('M', 'Micro'), ('N', 'Nano')], max_length=3)),
            ],
            bases=('content.digitalproduct',),
        ),
        migrations.CreateModel(
            name='Refrigerator',
            fields=[
                ('homeappliance_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.HomeAppliance')),
                ('voltage', models.SmallIntegerField()),
                ('side_by_side', models.BooleanField()),
                ('top_mount_freezer', models.BooleanField()),
            ],
            bases=('content.homeappliance',),
        ),
        migrations.CreateModel(
            name='Stationery',
            fields=[
                ('educational_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.Educational')),
                ('color', models.CharField(choices=[('black', 'black'), ('white', 'white'), ('silver', 'silver'), ('blue', 'blue'), ('red', 'red'), ('green', 'green'), ('yellow', 'yellow')], max_length=100)),
                ('kind', models.CharField(choices=[('pen', 'pen'), ('pencil', 'pencil'), ('Ravan_nevis', 'Ravan_nevis')], max_length=50)),
                ('nib', models.CharField(choices=[('flat', 'flat'), ('ballbearings', 'ballbearings')], max_length=50)),
            ],
            bases=('content.educational',),
        ),
        migrations.CreateModel(
            name='Television',
            fields=[
                ('homeappliance_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.HomeAppliance')),
                ('resolution', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=50)),
            ],
            bases=('content.homeappliance',),
        ),
    ]
