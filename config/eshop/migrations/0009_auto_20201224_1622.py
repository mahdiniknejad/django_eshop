# Generated by Django 3.1.4 on 2020-12-24 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0008_category_barand'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='barand',
            new_name='brand',
        ),
    ]
