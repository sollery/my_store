from django import forms
from .models import Order
from django.forms import TextInput, EmailInput, NumberInput, Select, RadioSelect, ModelForm


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'payment_method','delivery_method']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Емейл',
            'address': 'Адрес',
            'postal_code': 'Почтовый индекс',
            'city': 'Город',
            'payment_method': 'Способ оплаты',
            'delivery_method': 'Способ доставки',
        }
        help_text = {'first_name': 'Заполните имя', 'last_name': 'Из уже существующих'}

        widgets = {
            "first_name": TextInput(attrs={
                'placeholder': 'Ваше имя',
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
            "payment_method": RadioSelect(attrs={
                'class': 'my_radio',
                'placeholder': 'Способ оплаты'
            }),
            "delivery_method": RadioSelect(attrs={
                'class': 'my_radio',
                'fields': ['title','price_delivery'],
                'placeholder': 'Способ оплаты'
            }),

        }