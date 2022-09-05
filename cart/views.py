import json
from django.contrib.messages.storage import session
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm



# @require_POST
# def cart_add(request, id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=id)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product=product,
#                  quantity=cd['quantity'])
#         return redirect('cart_detail')
# def cart_remove(request, product_id):
#
#         # cart = Cart(request)
#         # product = get_object_or_404(Product, pk=product_id)
#         # cart.remove(product)
#     return render(request, 'detail.html')


# def cart_detail(request):
#     cart = Cart(request)
#     if request.method == 'POST':
#         temp = json.load(request)
#         product = get_object_or_404(Product, pk=temp['product_id'])
#         cart.remove(product)
#         new_cart = Cart(request)
#         print(temp)
#         print(new_cart.cart)
#         return HttpResponse(json.dumps(new_cart.cart))
#     return render(request, 'detail.html', {'cart': cart})


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


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'detail.html', {'cart': cart})


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
