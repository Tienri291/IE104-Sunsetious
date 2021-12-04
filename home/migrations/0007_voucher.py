# Generated by Django 3.2.6 on 2021-12-03 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_merge_0004_room_0005_product_n_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=40)),
                ('expiration_date', models.DateField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
    ]
