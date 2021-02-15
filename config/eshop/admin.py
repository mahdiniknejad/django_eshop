from django.contrib import admin
from .models import Product, Category, ProductGallery, ContactUs

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'get_category','price', 'get_image', 'status', 'active')
    list_filter = ('title', 'publish')
    search_fields = ('title', 'description')
    ordering = ['-status','-publish']

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'parent', 'active')
    list_filter = ('active',)
    search_fields = ('title',)
    ordering = ['-active']

admin.site.register(Category, CategoryAdmin)

class ProductGalleryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'title', ('product.title',)}

admin.site.register(ProductGallery)

admin.site.register(ContactUs)