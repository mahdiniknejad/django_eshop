# Generated by Django 3.1.4 on 2020-12-22 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'محصول', 'verbose_name_plural': 'محصولات'},
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(null=True, verbose_name='قیمت'),
        ),
    ]
