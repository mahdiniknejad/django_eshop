# Generated by Django 3.1.4 on 2020-12-23 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0006_auto_20201223_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(default=None, related_name='products', to='eshop.Category', verbose_name='دسته ها'),
        ),
    ]