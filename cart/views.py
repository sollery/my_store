import json
from django.contrib.messages.storage import session
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from .cart import Cart

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'detail.html', {'cart': cart})


def data_cart(request):
    cart = Cart(request)
    if request.method == 'POST':
        temp = json.load(request)
        product = get_object_or_404(Product, pk=temp['product_id'])
        if temp['change'] == 'plus':
            cart.plus(product)
        elif temp['change'] == 'minus':
            cart.minus(product)
        elif temp['change'] == 'del':
            cart.remove(product)
        elif temp['change'] == 'add':
            cart.add(product=product)
        cart = Cart(request)
        print(temp)
        print(cart.cart)

        # print(cart.get_total_price())
        # print(len(cart))
        in_cart = cart.cart.copy()
        in_cart['cart_total_price'] = cart.get_total_price()
        in_cart['cart_len'] = len(cart)
        # print(in_cart)
        # Источник: https: // pythonstart.ru / osnovy / iter - python

    return JsonResponse(in_cart)


def cart_clear(request):
    cart = Cart(request)
    text = 'произошла ошибка'
    data = json.load(request)
    if request.method == 'POST':
        print('----')
        print(data)
        print('----')
        if data.get('clear'):
            print('1')
            cart.clear()
            text = 'Корзина пуста'
        return HttpResponse(text)
