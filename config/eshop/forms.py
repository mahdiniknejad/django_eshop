from django import forms
from django.core import validators

class ContactUsForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder' : 'نام و نام خانوادگی خود را وارد کنید', 'class':'form-control'}),
        label='نام و نام خانوادگی',
    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder' : 'موضوع خود را وارد کنید', 'class':'form-control'}),
        label='موضوع',
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder' : 'ایمیل خود را وارد کنید', 'class':'form-control'}),
        label='ایمیل',
    )

    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder' : 'متن خود را وارد کنید', 'class':'form-control', 'id':'message', 'rows':'8'}),
        label='متن پیام',
    )



