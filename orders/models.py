from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from shop.models import Product


class DeliveryMethod(models.Model):
    title = models.CharField('Название',max_length=50)
    price_delivery = models.IntegerField('Цена доставки')

    class Meta:
        verbose_name = 'Способ доставки'
        verbose_name_plural = 'Способы доставки'

    def __str__(self):
        return self.title


class PaymentMethod(models.Model):
    title = models.CharField('Название',max_length=50)

    class Meta:
        verbose_name = 'Способ оплаты'
        verbose_name_plural = 'Способы'

    def __str__(self):
        return self.title


class Order(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    email = models.EmailField('Эл.адрес')
    address = models.CharField('Адрес',max_length=250)
    postal_code = models.CharField('Почтовый индекс',max_length=20)
    city = models.CharField('Город',max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    payment_method = models.ForeignKey(PaymentMethod,on_delete=models.CASCADE)
    delivery_method = models.ForeignKey(DeliveryMethod, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        if self.delivery_method.title == 'Курьером':
            return int(sum(item.get_cost() for item in self.items.all()) + self.delivery_method.price_delivery)
        return int(sum(item.get_cost() for item in self.items.all()))

    def order_pdf(self):
        return mark_safe('<a href="{}">PDF</a>'.format(
            reverse('admin_order_pdf', args=[self.id])))


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items',on_delete=models.CASCADE)
    price = models.FloatField(default=1)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
# Create your models here.
