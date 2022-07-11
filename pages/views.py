from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import Permission
from accounts.models import CustomUser
from shop.models import Product, ProductImage


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    products_images_phones = products_images.filter(product__category__id=1)
    return render(request, 'home.html', locals())


class AboutPageView(TemplateView):
    template_name = 'about.html'


