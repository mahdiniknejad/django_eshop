# Generated by Django 3.1.4 on 2021-01-11 17:47

from django.db import migrations, models
import eshop.models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0011_auto_20210109_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام و نام خانوادگی')),
                ('subject', models.CharField(max_length=50, verbose_name='موضوع')),
                ('title', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('description', models.TextField(verbose_name='شرح')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=eshop.models.unique_file_path, verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='productgallery',
            name='image',
            field=models.ImageField(upload_to=eshop.models.unique_file_path_gallery, verbose_name='تصویر'),
        ),
    ]