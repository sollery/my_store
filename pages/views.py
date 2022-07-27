from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import Permission
from accounts.models import CustomUser
from shop.models import Product, ProductImage
from cart.forms import CartAddProductForm


def home(request):
    products = Product.objects.all()[:4]
    cart_product_form = CartAddProductForm()
    return render(request, 'home.html', locals())


class AboutPageView(TemplateView):
    template_name = 'about.html'


