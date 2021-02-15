# Generated by Django 3.1.4 on 2021-02-03 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eshop', '0014_auto_20210203_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='viewer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='viewer', to=settings.AUTH_USER_MODEL),
        ),
    ]
