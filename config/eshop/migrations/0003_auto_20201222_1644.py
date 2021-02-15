# Generated by Django 3.1.4 on 2020-12-22 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0002_auto_20201222_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=False, verbose_name='آیا نمایش داده شود؟'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('p', 'موجود'), ('d', 'نا موجود'), ('f', 'بزودی')], max_length=1, verbose_name='وضعیت موجودی'),
        ),
    ]