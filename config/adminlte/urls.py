from django.urls import path
from .views import (
    ProductView,
    AddProduct, 
    UpdateProduct, 
    DeleteProduct,
    UserView,
    UpdateUser,
    DeleteUser,
    )

app_name = 'adminlte'

urlpatterns = [
    path('productsview/', ProductView.as_view(), name='productview'),
    path('addproduct/', AddProduct.as_view(), name='addproduct'),
    path('updateproduct/<int:pk>/', UpdateProduct.as_view(), name='updateproduct'),
    path('deleteview/<int:pk>/', DeleteProduct.as_view(), name='deleteview'),
#########################
    path('usersview/', UserView.as_view(), name='userview'),
    path('updateuser/<int:pk>/', UpdateUser.as_view(), name='updateuser'),
    path('deleteuser/<int:pk>/', DeleteUser.as_view(), name='deleteuser'),

]
