from django import forms
from django.core.exceptions import ValidationError

from .models import Order, DeliveryMethod
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

        }

    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['delivery_method'].help_text = 'Курьером стоимость - 300 рублей'

        print(self.fields['delivery_method'].help_text)

class Oplata(forms.Form):
    paid_order_sum = forms.IntegerField(label='Введите сумму к оплате')
    def clean_renewal_date(self):
        data = self.cleaned_data['paid_order_sum']
        #Проверка того, что дата не выходит за "нижнюю" границу (не в прошлом).
        if data < 0:
            raise ValidationError('Invalid date - renewal in past')
        #Проверка того, то дата не выходит за "верхнюю" границу (+4 недели).
        # Помните, что всегда надо возвращать "очищенные" данные.
        return data