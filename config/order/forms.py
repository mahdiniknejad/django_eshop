from django import forms

class Add_user_order(forms.Form):

    product_id = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    count = forms.IntegerField(
        widget = forms.NumberInput(attrs={'class':'search_box'}),
        initial=1,
    )