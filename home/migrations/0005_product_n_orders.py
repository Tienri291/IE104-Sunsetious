# Generated by Django 3.2.6 on 2021-12-03 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20211203_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='n_orders',
            field=models.IntegerField(default=0),
        ),
    ]
