# Generated by Django 4.1.5 on 2023-01-20 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApplication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hoteluser',
            name='image',
            field=models.BinaryField(max_length=100000),
        ),
    ]
