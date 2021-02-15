from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView, PasswordResetView

# Create your views here.


def loginView(request):
    if request.user.is_authenticated:
        return redirect('/')
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        uname = login_form.cleaned_data.get('username')
        passwd = login_form.cleaned_data.get('password')
        user = authenticate(request ,username=uname ,password=passwd)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            login_form.add_error('username', "نام کاربری یا رمزعبور نادرست است")
    context = {
        "login_form" : login_form
    }
    return render(request, 'shop/login.html', context)


def RegisterView(request):
    if request.user.is_authenticated:
        return redirect('/')
    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        uname = request.POST.get('username')
        passwd = request.POST.get('password')
        em = request.POST.get('email')
        User.objects.create_user(username=uname, password=passwd, email=em)
        return redirect('/')
    context = {
        'register_form' : register_form,
    }

    return render(request, 'shop/register.html', context)

class change_password_view(PasswordChangeView):

    success_url = reverse_lazy('account:password_change_done')
