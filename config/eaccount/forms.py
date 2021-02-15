from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder' : 'نام کاربری', 'class':'mahdi'}),
        label='نام کاربری',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder' : 'رمز عبور'}),
        label='رمز عبور',
    )


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder' : 'نام کاربری'}),
        label='* نام کاربری',
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder' : 'پست الکترونیکی'}),
        label='* پست الکترونیکی',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder' : 'رمز عبور'}),
        label='* رمز عبور',
    )
    repassword = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder' : 'تکرار رمز عبور'}),
        label='* تکرار رمز عبور',
    )

    def clean_username(self):
        uname = self.cleaned_data.get('username')
        exist_username = User.objects.filter(username=uname)
        if len(exist_username) == 0:
            pass
        else:
            raise forms.ValidationError('نام کاربری موجود است')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        exist_email = User.objects.filter(email=email)
        if len(exist_email) == 0:
            pass
        else:
            raise forms.ValidationError('پست الکترونیکی موجود است')

    def clean_repassword(self):
        passwd1 = self.cleaned_data.get('password')
        passwd2 = self.cleaned_data.get('repassword')
        if passwd1 != passwd2:
            raise forms.ValidationError('تکرار کلمه عبور صحیح نیست')