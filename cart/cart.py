from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart:
    def __init__(self, request):
        """Инициализация объекта корзина."""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def save(self):
        """Сохранение изменений в корзине"""
        # Помечаем сессию как измененную
        self.session.modified = True

    def add(self, product):
        """Добавление товара в корзину"""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1, 'price': str(product.price), 'name': product.name}
        self.save()

    def plus(self, product):
        """Увеличивает количество товара"""
        # добавление товара в корзине
        product_id = str(product.id)
        self.cart[product_id]['quantity'] += 1
        self.save()

    def minus(self,product):
        """Уменьшает количество товара"""
        # удаление товара в корзине
        product_id = str(product.id)
        if self.cart[product_id]['quantity'] > 1:
            self.cart[product_id]['quantity'] -= 1
            self.save()
        else:
            del self.cart[product_id]
            self.save()

    def clear(self):
        """Очищает корзину"""
        # Очистка корзины.
        del self.session[settings.CART_SESSION_ID]
        self.save()



    def remove(self, product):
        """Удаление товара из корзины."""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    def __iter__(self):
        """Проходим по товарам корзины и получаем соответствующие объекты Product."""
        product_ids = self.cart.keys()
        # Получаем объекты модели Product и передаем их в корзину.
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = int(float(item['price']))
            item['total_price'] = int(float(item['price'] * item['quantity']))
            yield item

    def __len__(self):
        """Возвращает общее количество товаров в корзине."""
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """Возвращает общую сумму товаров в корзине."""
        return sum(
            int(float(item['price'])) * item['quantity'] for item in self.cart.values()
        )




