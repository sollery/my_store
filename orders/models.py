import random
import string

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
        db_table = 'DeliveryMethod'

    def __str__(self):
        return self.title


class PaymentMethod(models.Model):
    title = models.CharField('Название',max_length=50)

    class Meta:
        verbose_name = 'Способ оплаты'
        verbose_name_plural = 'Способы'
        db_table = 'PaymentMethod'

    def __str__(self):
        return self.title


def create_code():
    random_list = list(string.ascii_uppercase) + list(string.digits) + list(string.ascii_lowercase)
    thepassword = ""
    length = 6
    for i in range(length):
        thepassword += random.choice(random_list)
    # order_code = None
    # try:
    #     order_code = Order.objects.get(code=order_code)
    # except Order.DoesNotExist:
    #     pass
    # if order_code is not None:
    return thepassword



class Order(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    email = models.EmailField('Эл.адрес')
    address = models.CharField('Адрес',max_length=250)
    city = models.CharField('Город',max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    payment_method = models.ForeignKey(PaymentMethod,on_delete=models.CASCADE)
    delivery_method = models.ForeignKey(DeliveryMethod, on_delete=models.CASCADE)
    code = models.CharField('Cекретный ключ',max_length=6, default=create_code())


    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        db_table = 'Order'

    def __str__(self):
        return 'Заказ номер: {}'.format(self.id)

    def check_delivery_method(self):
        if self.delivery_method.title.lower() == 'курьером':
            return True
        return False

    def get_total_cost(self):
        if self.check_delivery_method():
            return int(sum(item.get_cost() for item in self.items.all()) + self.delivery_method.price_delivery)
        return int(sum(item.get_cost() for item in self.items.all()))

    def order_pdf(self):
        return mark_safe('<a href="{}">PDF</a>'.format(
            reverse('admin_order_pdf', args=[self.id])))

    def check_payment_method(self):
        if self.payment_method.title.lower() == "картой":
            return True
        return False



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE,verbose_name='Номер заказа')
    product = models.ForeignKey(Product, related_name='order_items',on_delete=models.CASCADE,null=True,
                                verbose_name='Название продукта')
    price = models.IntegerField('Цена')
    quantity = models.PositiveIntegerField('Кол-во')


    class Meta:
        db_table = 'OrderItem'

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
# Create your models here.
