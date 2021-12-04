# Generated by Django 3.2.9 on 2021-12-03 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
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