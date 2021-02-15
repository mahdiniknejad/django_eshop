from django.shortcuts import render, get_object_or_404, Http404
from django.views.generic import ListView, DetailView
from .models import Product, Category, ProductGallery, ContactUs, viewer
import itertools
from order.forms import Add_user_order
from .forms import ContactUsForm


def mygrouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e != None] for t in itertools.zip_longest(*args))
  


# Create your views here.

class MainShop(ListView):
    template_name = 'shop/index.html'
    def get_queryset(self):
        return Product.objects.active_product().order_by('-publish')

class ProductDitail(DetailView):
    template_name = 'shop/product-details.html'

    def get_object(self):
        slug = self.kwargs.get('slug')
        global data
        data = get_object_or_404(Product, slug=slug, active=True)

        view = viewer.objects.filter(user_id=self.request.user.pk, product_id=data.pk).first()
        if view is None:
            viewer.objects.create(user_id=self.request.user.pk, product_id=data.pk)
            data.view_count += 1
            data.save()

        return data

    def get_context_data(self, *args, **kwargs):
        UserOrder = Add_user_order(self.request.POST or None, initial={'product_id' : data.pk})
        context = super(ProductDitail, self).get_context_data(**kwargs)
        value = mygrouper(3, ProductGallery.objects.filter(product_id=data.pk))
        context['mygallery'] = value
        context['UserOrder'] = UserOrder
        return context

def CategoryView(request, slug):
    cat = get_object_or_404(Category, slug=slug, active=True)
    context = {
        'category' : cat,
        'object_list' : cat.products.active_product(),
        'categoris' : Category.objects.filter(active=True)
    }
    return render(request, 'shop/shop.html', context)

def brandsView(request):
    context = {
        'categoris' : Category.objects.filter(active=True)
    }
    return render(request, 'shop/renderpartials/brands.html', context)


def category_module_View(request):
    context = {
        'categoris' : Category.objects.filter(active=True)
    }
    return render(request, 'shop/renderpartials/category_moduls.html', context)

def sliderView(request):
    context = {
        'slider' : Product.objects.active_product().order_by('-publish')[:3] 
    }
    return render(request, 'shop/slider.html', context)

class SearchView(ListView):
    template_name = 'shop/shop.html'
    def get_queryset(self):
        result = self.request.GET.get('search')
        if(result is not None):
            return Product.objects.filter(title__contains=result)
        else:
            return None


def contactUsView(request):

    contact_form = ContactUsForm(request.POST or None)
    if contact_form.is_valid():
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        text = request.POST.get('text')
        ContactUs.objects.create(name=name, subject=subject, title=email, description=text)
    
    context = {
        'contact_form':contact_form,
    }
    return render(request, 'shop/contact-us.html', context)