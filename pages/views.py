from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import Permission
from accounts.models import CustomUser
from shop.models import Product, ProductImage, Rating, Favorites
from cart.forms import CartAddProductForm
from shop.models import Category
from cart.cart import Cart

def home(request):
    products = Product.objects.all().order_by('created')[:4]
    products_rating = Rating.objects.all().order_by('value').values('product_id')
    print(products_rating)
    cart_product_form = CartAddProductForm()
    context = {'products':products,'products_rating':products_rating,'cart_product_form':cart_product_form}
    # category_list = Category.objects.all()
    # paginator = Paginator(products, 4)
    #
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', locals())


class AboutPageView(TemplateView):
    template_name = 'about.html'


def check_favorites(request):
    context = {'text':'для добавление в избранное нужна авторизация'}
    if request.user.is_authenticated:
        favorites = Favorites.objects.filter(user=request.user)
        print('*********')
        print(request.user)
        print(favorites)
        print('*********')
        return render(request, 'favorites.html', {'favorites': favorites})
    return render(request, 'favorites.html', context)
