# Generated by Django 3.1.7 on 2021-04-21 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_subcategory_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, db_index=True, null=True, verbose_name='Цена'),
        ),
    ]
