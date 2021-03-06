# Generated by Django 3.1.4 on 2021-01-09 16:01

from django.db import migrations, models
import django.db.models.deletion
import eshop.models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0009_auto_20201224_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=eshop.models.unique_file_path, verbose_name='تصویر')),
                ('title', models.CharField(default='product', max_length=50, verbose_name='نام')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='eshop.product', verbose_name='محصول مرتبط')),
            ],
        ),
    ]
