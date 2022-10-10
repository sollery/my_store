import json

from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import Permission
from accounts.models import CustomUser
from shop.models import Product, ProductImage, Rating, Favorites
from cart.forms import CartAddProductForm
from shop.models import Category
from cart.cart import Cart

def home(request):
    products = Product.objects.all().order_by('-created')[:4]
    products_rating = Rating.objects.all().order_by('-value').values('product_id','value')
    # print(products_rating)
    cart_product_form = CartAddProductForm()
    context = {'products':products,'products_rating':products_rating,'cart_product_form':cart_product_form}
    # category_list = Category.objects.all()
    # paginator = Paginator(products, 4)
    #
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    try:
        favorites = Favorites.objects.filter(Q(user=request.user)).values('product_id')
        fav_product = [item.get('product_id') for item in favorites]
    except:
        fav_product = []
    print(products_rating)
    print(fav_product)
    for product in products:
        print(product.id)

    return render(request, 'home.html', locals())


class AboutPageView(TemplateView):
    template_name = 'about.html'


def check_favorites(request):
    context = {'text':'для добавление в избранное нужна авторизация'}
    if request.user.is_authenticated:
        favorites = Favorites.objects.filter(user=request.user)
        paginator = Paginator(favorites, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        print('*********')
        print(request.user)
        print(favorites)
        print('*********')
        return render(request, 'favorites.html', {'page_obj': page_obj})
    return render(request, 'favorites.html', context)


def change_favorites(request):
    if request.method == 'POST':
        temp = json.load(request)
        user = request.user
        product = None
        if temp.get('product_id'):
            product = Product.objects.get(pk=int(temp.get('product_id')))
        print('*********')
        print(temp)
        print('*********')
        text = ''
        if temp.get('change') == 'add':
            try:
                favorite = Favorites(user=user,product=product)
                if Favorites.objects.filter(Q(user=user) & Q(product=product)):
                    text = 'Товар уже в избранном'
                else:
                    favorite.save()
                    text = 'Товар добавлен в избранное'
            except:
                text = 'Произошла ошибка'
        elif temp.get('change') == 'del':
            try:
                favorite_del = Favorites.objects.filter(Q(user=user) & Q(product=product))
                print(Favorites.objects.filter(Q(user=user) & Q(product=product)).values())
                favorite_del.delete()
                text = 'Товар удален из избранного'
            except:
                text = 'Произошла ошибка'
        elif temp.get('change') == 'clear':
            try:
                favorites = Favorites.objects.all()
                favorites.delete()
                text = 'Все товары удаленны из избранного'
            except:
                text = 'Произошла ошибка'
        favorites_all = Favorites.objects.filter(user=user).count()
        print('ggg')
        print(favorites_all)
        favorites_info = {'text' : text,
                          'favorites_count': favorites_all
                          }
        return JsonResponse(favorites_info)