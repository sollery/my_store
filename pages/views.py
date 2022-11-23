import json
import random
import string

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.core.mail import EmailMessage
from django.core.paginator import Paginator
from django.db.models import Q, Max, Min, Count
from django.forms import formset_factory
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.models import Permission
from accounts.models import CustomUser
from shop.models import Product, ProductImage, Rating, Favorites,ProductRecommendations,CategoryImage,MessageFromUser,MessageAnswerForUser

from shop.models import Category
from cart.cart import Cart
from alert_admin_bot.send_message_bot import send_alert_bot
from orders.models import Order,OrderItem

from .forms import ProductForm, ProductImgForm, CategoryForm, CategoryImgForm, \
    MessageForUserForm, MessageAnswerForUserForm, CheckStatusOrder


def home(request):
    """"Функция отображения главной страницы"""
    # products = Product.objects.all().order_by('-created')[:4]
    products_rating = Rating.objects.all().order_by('-value').values('product_id','value')
    # print(products_rating)
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
    # print(products_rating)
    # print(fav_product)
    # for product in products:
    #     # print(product.id)

    # random_list = list(string.ascii_uppercase) + list(string.digits) + list(string.ascii_lowercase)
    # thepassword = ""
    # length = 6
    # for i in range(length):
    #     thepassword += random.choice(random_list)
    # print(thepassword)
    products = Product.objects.filter(active=True).annotate(cnt=Count('order_items')).order_by('-cnt')[:4]
    print(OrderItem.objects.filter(product__name='iphone 13').count())
    return render(request, 'home.html', locals())


class AboutPageView(TemplateView):

    template_name = 'about.html'


def check_favorites(request):
    """Функция проверяет есть ли у пользователя товары в избранном"""
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
        temp = False
        if favorites:
            temp = True

        return render(request, 'favorites.html', {'page_obj': page_obj,'temp':temp})
    return render(request, 'favorites.html', context)


def change_favorites(request):
    """Функция для изменений в избранных товарах пользователя"""
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


def main_shop(request):
    return render(request,'main.html')


@staff_member_required
def panel(request):
    """Функция для отображения кастомной панели администратора"""
    return render(request, 'my_shop_admin_panel.html')


@staff_member_required
def orders_list(request):
    """Функция для списка заказов пользователей"""
    orders_list = Order.objects.all()
    paginator = Paginator(orders_list,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'orders.html', {'page_obj': page_obj})


@staff_member_required
def order_detail(request,id):
    """Функция для отображения конкретного заказа"""
    order = OrderItem.objects.filter(order_id=id).values('product__name','price','quantity')
    print(order)
    sum = Order.objects.get(pk=id).get_total_cost()
    print(sum)
    order_id = id
    return render(request, 'order_detail.html', {'order': order,'sum': sum,'order_id':order_id})

@staff_member_required
def create_product(request):
    """Функция для создания товара"""
    form = ProductForm()
    if request.method == "POST":
        print('10')
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            product_id = Product.objects.get(name=product_name)
            print(product_id)
            # return redirect('home')
            return redirect(f'/upl_img_product/{int(product_id.id)}/')
    return render(request,'create_product.html',{'form':form})



@staff_member_required
def create_category(request):
    """Функция для создания категории"""
    form = CategoryForm()
    if request.method == "POST":
        print('10')
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            category_name = form.cleaned_data.get('name')
            category = Category.objects.get(name=category_name)
            return redirect(f'/upl_img_category/{int(category.id)}/')
    return render(request,'create_category.html',{'form':form})


@staff_member_required
def upl_img_product(request,pk):
    """Функция для добавления фото к новому товару"""
    ProductImgFormFormset = formset_factory(ProductImgForm, extra=3)
    formset = ProductImgFormFormset()
    if request.method == 'POST':
        ProductImgFormFormset = formset_factory(ProductImgForm)
        formset = ProductImgFormFormset(request.POST, request.FILES)
        product = Product.objects.get(id=pk)
        product_slug = product.slug
        if formset.is_valid():
            for form in formset:
                print(form)
                main = form.cleaned_data.get('main')
                img = form.cleaned_data.get('image')

                ProductImage.objects.create(main=main,image=img,product=product)
            return redirect(f'/shop/products/{pk}/{product_slug}/')
    return render(request,'upl_img_product.html',{'formset':formset})

@staff_member_required
def upl_img_category(request,pk):
    """Функция для добавления фото к новой категории"""
    form = CategoryImgForm()
    if request.method == 'POST':
        form = CategoryImgForm(request.POST, request.FILES)
        category = Category.objects.get(id=pk)
        if form.is_valid():
            img = form.cleaned_data.get('image')
            CategoryImage.objects.create(image=img,category=category)
            return redirect(category.get_absolute_url())
    return render(request, 'upl_img_category.html', {'form': form})



def create_message_from_user(request):
    """Функция отвечает за отображения страницы создания обращения от пользователя и создание самого обращения"""
    form = MessageForUserForm()
    if request.method == "POST":
        print('10')
        form = MessageForUserForm(request.POST)
        if form.is_valid():
            print(request.POST)
            text = form.cleaned_data.get('text')
            email = form.cleaned_data.get('email')
            title = form.cleaned_data.get('title')
            new_mes = MessageFromUser.objects.create(title=title,text=text,email=email)
            link_mes = f' http://127.0.0.1:8000{new_mes.get_absolute_url()}'
            send_alert_bot(link_mes,'Обращение')
            return redirect('home')
    return render(request, 'create_user_message.html', {'form': form})

@staff_member_required
def user_message_list(request):
    """Функция отвечает за отображения всех обращений пользователей"""
    message_list = MessageFromUser.objects.all().order_by('-created')
    paginator = Paginator(message_list,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'message_list.html', {'page_obj': page_obj})

@staff_member_required
def user_message_detail(request,pk):
    """Функция отвечает за отображение конкретного обращения"""
    answer = None
    message = MessageFromUser.objects.get(id=pk)
    if message.status:
        answer = MessageAnswerForUser.objects.get(message_user=message)
    return render(request, 'message_detail.html', {'message': message,'answer':answer})


@staff_member_required
def create_answer_message_for_user(request,pk):
    """Функция за о"""
    form = MessageAnswerForUserForm()
    if request.method == "POST":
        print('10')
        form = MessageAnswerForUserForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            message_user = MessageFromUser.objects.get(id=pk)
            MessageAnswerForUser.objects.create(text=text,message_user=message_user)
            message_user.status = True
            message_user.save()
            subject = 'My-shop - Ответ на ваше обращение'
            message = form.cleaned_data.get('text')

            email = EmailMessage(subject,
                                 message,
                                 'ilushamdmaa@yandex.ru',
                                 [message_user.email])
            email.send()

            return redirect('message_list')
    return render(request, 'message_answer.html', {'form': form})

class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect('/admin/')


class ProductUpdateView(SuperUserRequiredMixin,UpdateView):
    model = Product
    template_name = 'edit_product.html'
    fields = ['description', 'price', 'active']


def check_status_order(request):
    form = CheckStatusOrder()
    return render(request, 'check_status_order.html', {'form': form})


def status_data(request):
    if request.method == 'POST':
        temp = json.load(request)
        number = temp.get('number')
        email = temp.get('email').lower()
        try:
            order = Order.objects.get(pk=number,email=email)
            data = f'{order.status}'
        except Order.DoesNotExist:
            data = 'Не соответствие введенных данных'
        return HttpResponse(data)


