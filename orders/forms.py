from django import forms
from .models import Order
from django.forms import TextInput, EmailInput, NumberInput,Select

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'payment_method']

        widgets = {
            "first_name": TextInput(attrs={
                'class': 'myfield',
                'placeholder': 'Ваше имя'
            }),
            "last_name": TextInput(attrs={
                'class': 'myfield',
                'placeholder': 'Ваша фамилия'
            }),
            "email": EmailInput(attrs={
                'class': 'myfield',
                'placeholder': 'Ваша почта'
            }),
            "address": TextInput(attrs={
                'class': 'myfield',
                'placeholder': 'Ваше адрес'
            }),
            "postal_code": TextInput(attrs={
                'class': 'myfield',
                'placeholder': 'Ваш почтовый индекс'
            }),
            "city": TextInput(attrs={
                'class': 'myfield',
                'placeholder': 'Ваш город'
            }),
            "payment_method": Select(attrs={
                'class': 'myfield',
                'placeholder': 'Способ оплаты'
            }),

        }