from django.urls import path
from .views import (
    MainShop,
    ProductDitail,
    CategoryView,
    brandsView,
    sliderView,
    SearchView,
    contactUsView,
    category_module_View,
)

app_name = "shop"


urlpatterns = [
    path('', MainShop.as_view(), name="home" ),
    path('product/<slug:slug>/', ProductDitail.as_view(), name="detail" ),
    path('category/<slug:slug>/', CategoryView, name="category" ),
    path('render-partials/empty/none/false/', brandsView, name="brands"),
    path('render-partials/empty/none/false/3/5/', category_module_View, name="category_module"),
    path('render-partials/empty/none/false/2/', sliderView, name="sliders"),
    path('search/', SearchView.as_view(), name="search"),
    path('contact-us/', contactUsView, name="contact"),
]
