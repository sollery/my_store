from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse




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

