# Generated by Django 3.2.9 on 2021-12-04 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_merge_0004_room_0005_product_n_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('stars', models.DecimalField(decimal_places=1, max_digits=5)),
                ('n_reviews', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('views', models.IntegerField()),
                ('location', models.CharField(max_length=30)),
            ],
        ),
    ]