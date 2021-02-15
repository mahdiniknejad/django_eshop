from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from django.shortcuts import reverse
from os.path import splitext
from random import randint
from django.contrib.auth.models import User
import os
# Create your models here.


def unique_file_path_gallery(instance, filename):
    # Save original file name in model
    instance.original_file_name = filename

    # Get new file name/upload path
    base, ext = splitext(filename)
    newname = "%s%s%s%s" % (str(randint(755, 888854)), str(randint(755, 888854)), str(randint(755, 888854)), ext)
    return os.path.join('product_images/gallery/', newname)
    # return 'product_images/gallery/'

def unique_file_path(instance, filename):
    # Save original file name in model
    instance.original_file_name = filename

    # Get new file name/upload path
    base, ext = splitext(filename)
    newname = "%s%s%s" % (str(randint(755, 888854)), str(randint(755, 888854)), ext)
    return os.path.join('product_images/', newname)
    # return 'product_images/gallery/'


class ProductManager(models.Manager):
    
    def active_product(self):
        return self.get_queryset().filter(active=True)


class Category(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False, verbose_name='نام')
    slug = models.SlugField(max_length=50, null=False, unique=True, verbose_name='دامنه')
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='children', verbose_name='گروه اصلی')
    active = models.BooleanField(default=False, verbose_name='آیا نمایش داده شود؟')
    brand = models.BooleanField(default=False, verbose_name='آیا این دسته نام برند است ؟')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته'
        verbose_name_plural = 'دسته ها'

    def get_url(self):
        return './category/{}'.format(self.slug)

    def get_children(self):
        return Category.objects.filter(parent=self)


class Product(models.Model):

    STATUS_CHOICES = (
        ('p', 'موجود'),
        ('d', 'نا موجود'),
        ('f', 'بزودی'),
    )

    title = models.CharField(max_length=50, blank=False, null=False, verbose_name='نام')
    slug = models.SlugField(max_length=50, null=False, unique=True, verbose_name='دامنه')
    price = models.IntegerField(null=True, verbose_name='قیمت')
    description = models.TextField(verbose_name='شرح')
    image = models.ImageField(upload_to=unique_file_path, verbose_name='تصویر')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار محصول')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت موجودی')
    active = models.BooleanField(default=False, verbose_name='آیا نمایش داده شود؟')
    category = models.ManyToManyField(Category, default=None, related_name='products', verbose_name='دسته ها')
    view_count = models.IntegerField(default=0, verbose_name="بازدید")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def get_image(self):
        return format_html("<img src={} width='100px;' alt='{}'>".format(self.image.url, self.title))
    get_image.short_description = 'تصویر'

    def get_category(self):
        categoris = []
        for i in self.category.all():
            categoris.append(i.title)
        return " - ".join(categoris)

    def get_absolute_url(self):
        return reverse('adminlte:info')

    objects = ProductManager()


class ProductGallery(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False, verbose_name='نام')
    image = models.ImageField(upload_to=unique_file_path_gallery, verbose_name='تصویر')
    product = models.ForeignKey(Product, on_delete=models.CASCADE ,verbose_name='محصول مرتبط', related_name='gallery')


    class Meta:
        verbose_name = 'گالری'
        verbose_name_plural = 'گالری ها'
    
    def __str__(self):
        return self.title


class ContactUs(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name='نام و نام خانوادگی')
    subject = models.CharField(max_length=50, blank=False, null=False, verbose_name='موضوع')
    title = models.EmailField(blank=False, null=False, verbose_name='ایمیل')
    description = models.TextField(verbose_name='شرح')


    class Meta:
        verbose_name = 'اطلاع'
        verbose_name_plural = 'اطلاعات'
    
    def __str__(self):
        return self.subject

class viewer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="بازدید کننده", related_name='viewer')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول دیده شده")
