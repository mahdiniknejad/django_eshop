from django.urls import path
from .views import user_order, order_list, delete_order_detail

app_name = 'order'

urlpatterns = [
    path('add-user-order/', user_order, name="add-user-order"),
    path('order_check/', order_list, name="order_list"),
    path('delete_order_check/<id>/', delete_order_detail, name="delete_order_detail"),
]