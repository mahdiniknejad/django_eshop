# Generated by Django 3.1.4 on 2021-02-03 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eshop', '0013_auto_20210111_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='view_count',
            field=models.IntegerField(default=0, verbose_name='بازدید'),
        ),
        migrations.AddField(
            model_name='product',
            name='viewer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]