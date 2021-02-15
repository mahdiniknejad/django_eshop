from django.urls import path
from .views import loginView, RegisterView, change_password_view

app_name = "account"


urlpatterns = [
    path('login/', loginView, name="login" ),
    path('signup/render-partial/', RegisterView, name="register" ),
]

from django.contrib.auth import views

urlpatterns += [
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('password_change/', change_password_view.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]

