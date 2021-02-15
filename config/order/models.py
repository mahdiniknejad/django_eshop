from django.db import models
from django.contrib.auth.models import User
from eshop.models import Product

# Create your models here.


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="مالک", related_name='order')
    is_pade = models.BooleanField(default=False, verbose_name="آیا پرداخت شده؟")
    payment_date = models.DateTimeField(null=True, blank=True, verbose_name="زمان پرداخت")

    def __str__(self):
        return self.owner.get_full_name()

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید'




class Order_detail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE ,verbose_name="مالک", related_name='order_detail')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول انتخاب شده")
    price = models.IntegerField(verbose_name="قیمت")
    count = models.IntegerField(verbose_name="تعداد")

    def __str__(self):
        return self.product.title

    def sum_price(self):
        return self.count * self.price

    class Meta:
        verbose_name = 'جزییات سبد'
        verbose_name_plural = 'جزییات سبد ها'
