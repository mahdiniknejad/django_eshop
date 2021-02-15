# Generated by Django 3.1.4 on 2020-12-23 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0003_auto_20201222_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='نام')),
                ('slug', models.SlugField(unique=True, verbose_name='دامنه')),
                ('active', models.BooleanField(default=False, verbose_name='آیا نمایش داده شود؟')),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='eshop.category')),
            ],
            options={
                'verbose_name': 'دسته',
                'verbose_name_plural': 'دسته ها',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='eshop.Category', verbose_name='دسته ها'),
        ),
    ]
