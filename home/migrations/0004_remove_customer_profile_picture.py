# Generated by Django 3.2.6 on 2021-12-05 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_order_orderitem_voucher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='profile_picture',
        ),
    ]
