# Generated by Django 3.1.7 on 2021-04-19 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210419_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Популярность товара'),
        ),
    ]
