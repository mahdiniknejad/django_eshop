from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import Add_user_order
from .models import Order, Order_detail
from eshop.models import Product
from django.shortcuts import Http404
# Create your views here.

@login_required(login_url='/user/login/')
def user_order(request):

    UserOrder = Add_user_order(request.POST or None)

    if UserOrder.is_valid():
        order = Order.objects.filter(owner_id=request.user.pk, is_pade=False).first()
        if(order is None):
            order = Order.objects.create(owner_id=request.user.pk, is_pade=False)

        product_id = UserOrder.cleaned_data.get('product_id')
        count = UserOrder.cleaned_data.get('count')
        if count <= 0:
            count = 1
        product = Product.objects.get(id=product_id)
        order_list = [i.product_id for i in order.order_detail.all()]
        if product.pk not in order_list:
            Order_detail.objects.create(price=product.price, count=count, product_id=product_id, order_id=order.pk)
        else:
            Order_detail.objects.filter(product_id=product_id, order_id=order.pk).delete()
            Order_detail.objects.create(price=product.price, count=count, product_id=product_id, order_id=order.pk)
    return redirect('/')

@login_required(login_url='/user/login/')
def order_list(request):

    order = Order.objects.filter(owner_id=request.user.pk, is_pade=False).first()


    total_price = 0
    for od in order.order_detail.all():
        total_price += od.price * od.count

    _9percent = ( (total_price/100) * 9 )

    if total_price >= 1000000:
        haml_va_naql = 0
    elif total_price == 0:
        haml_va_naql = 0
    else:
        haml_va_naql = 50000

    context = {
        'order_list' : order.order_detail.all(),
        'total_price_1' : total_price,
        'total_price_2' : total_price +  _9percent + haml_va_naql,
        'p_9percent' : _9percent,    
        'haml_va_naql' : haml_va_naql
    }

    return render(request, 'order/cart.html', context)
# -----------------------------------------------------------------
@login_required(login_url='/user/login/')
def delete_order_detail(request, *args, **kwargs):

    order_detail_id = kwargs.get('id') 
    order = Order.objects.filter(owner_id=request.user.pk, is_pade=False).first()
    p = order.order_detail.filter(pk=order_detail_id)
    if p is not None:
        p.delete()
    else:
        raise Http404('صفحه یافت نشد')

    return redirect('/order_check/')