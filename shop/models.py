from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
import datetime

from django.utils import timezone

from shop.managers import DiscountActiveManager


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    slug = models.SlugField(max_length=200, db_index=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=1)
    count = models.PositiveIntegerField('Кол-во товара', default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # discount = models.IntegerField('Скидка в процентах', blank=True, default=0)
    end_price = models.IntegerField('Итоговая цена', default=0)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.slug])

    def get_id(self):
        return str(self.pk)



    @property
    def discount_check(self):
        try:
            sale = Discount_product.disc_objects.get(product_id=self.pk)
        except Discount_product.DoesNotExist:
            sale = None
        return sale

    @property
    def get_sale(self):
        if self.discount_check is not None:
            return int(self.price * (100 - self.discount_check.get_discount_value) / 100)
        return self.price
        # lst_v = Discount_product.objects.filter(product_id=self.pk).values('discount__value')
        # print('---')
        # print(lst_d)
        # print('---')
    #     discount_product_list = Discount_product.objects.all().values('product_id')
    #     print('----')
    #     print(discount_product_list)
    #     lst_d = [i['product_id'] for i in discount_product_list]
    #     if
    # def save(self, *args, **kwargs):
    #     """Расчитать стоимость со скидкой"""
    #
    #     self.end_price = int(self.price * (100 - self.discount) / 100)
    #     super().save(*args, **kwargs)


class Review(models.Model):
    Product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='reviews',)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,)
    review = models.TextField('Отзыв')
    active = models.BooleanField(default=True)
    created_rew = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_rew = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return 'Отзыв от {} о {}'.format(self.author, self.Product)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.image

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Rating(models.Model):
    value = models.SmallIntegerField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    voted_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Discount(models.Model):
    value = models.IntegerField('Скидка в процентах', blank=True, default=0)

    class Meta:
        ordering = ('value',)
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    def __str__(self):
        return f"{self.value}%"


class Discount_product(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None,on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, blank=True, null=True, default=None, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    start = models.DateTimeField(default=timezone.now())
    end = models.DateTimeField(default=timezone.now())
    objects = models.Manager()
    disc_objects = DiscountActiveManager()

    class Meta:
        verbose_name = 'Скидка и название товара'
        verbose_name_plural = 'Скидки и название товара'

    def __str__(self):
        return f"{self.product.id}"

    @property
    def get_discount_value(self):
        return self.discount.value

    # class DiscountManager(models.Manager):
    #     def get_queryset(self):
    #         return super.get_queryset().filter(product_id=self.product.id)

  # discount_product_list = Discount_product.objects.all().values('product_id')
  #   print('----')
  #   print(discount_product_list)
  #   lst_d = [i['product_id'] for i in discount_product_list]
  #   print(lst_d)
  #   print('----')

