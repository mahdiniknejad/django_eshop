from django.shortcuts import render, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from eshop.models import Product
from .mixins import SuperuserMixin

from django.contrib.auth.models import User
# Create your views here.

class ProductView(LoginRequiredMixin, ListView):
    template_name = 'adminlte/pages/showproduct.html'
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Product.objects.all().order_by('-active','-publish')

class AddProduct(LoginRequiredMixin, SuperuserMixin, CreateView):
    template_name = 'adminlte/pages/addproduct.html'
    fields = [ "title", "slug", "price", "description", "image", "publish", "status", "active", "category"]
    model = Product

class UpdateProduct(LoginRequiredMixin, SuperuserMixin, UpdateView):
    template_name = 'adminlte/pages/addproduct.html'
    model = Product
    fields = [ "title", "slug", "price", "description", "image", "publish", "status", "active", "category"]
    success_url = reverse_lazy('adminlte:productview')
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Product, pk=pk)

class DeleteProduct(LoginRequiredMixin, SuperuserMixin, DeleteView):
    template_name = 'adminlte/pages/deleteproduct.html'
    model = Product
    success_url = reverse_lazy('adminlte:productview')
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Product, pk=pk)

class UserView(LoginRequiredMixin, SuperuserMixin, ListView):
    template_name = 'adminlte/pages/showproduct.html'
    def get_queryset(self):
        return User.objects.all().order_by('-pk')

class UpdateUser(LoginRequiredMixin, SuperuserMixin, UpdateView):
    template_name = 'adminlte/pages/addproduct.html'
    fields = [ "username", "first_name", "last_name", "email", "is_staff", "is_active", ]
    model = User
    success_url = reverse_lazy('adminlte:userview')
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(User, pk=pk)

class DeleteUser(LoginRequiredMixin, SuperuserMixin, DeleteView):
    template_name = 'adminlte/pages/deleteproduct.html'
    model = User
    success_url = reverse_lazy('adminlte:userview')
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(User, pk=pk)

