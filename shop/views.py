import json
from datetime import datetime
from django.contrib.admin.views.decorators import staff_member_required
from django.core import paginator
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.forms import model_to_dict, formset_factory
from django.template.loader import render_to_string
from django.views import View
from alert_admin_bot.send_message_bot import send_alert_bot
from orders.models import Order
from tzlocal import get_localzone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Avg, Count, When, Case, Value
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.generic import DetailView, ListView, UpdateView
from .forms import ChoiceSort, ReviewForm
from shop.models import Product, Category, Review, ProductImage, Rating, Discount_product,ProductRecommendations


def check_parent_or_children(product):
    if ProductRecommendations.objects.filter(Q(parent_id=product.pk) & Q(parent__active=True)):
        return True
    else:
        return False


def product_detail(request, pk, slug):
    """Функция отображения информации конкретного товара"""
    # reviews = Review.objects.filter(Product_id=pk)
    # print(reviews)
    product = None

    if request.user.is_superuser:
        product = get_object_or_404(Product, id=pk, slug=slug)
    else:
        product = get_object_or_404(Product, id=pk, slug=slug, active=True)
    # reviews = product.reviews.filter(active=True)
    # print(reviews)
    review_form = ReviewForm()
    check_fav = product.check_favorites(request.user)
    print('avg')
    # print(product.get_avg_rating)
    print('avg')
    print(check_fav)
    print(product.get_image_main)
    print(product.get_absolute_url())
    # product_img=product.objects.filter(productimage__main=True)
    # print(product_img)
    # paginator = Paginator(reviews, 2)
    # #
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    # if request.method == 'POST':
    #     # A comment was posted
    #     review_form = ReviewForm(data=request.POST)
    #     print(request.POST)
    #     print(request.user)
    #
    #     if review_form.is_valid():
    #         # Create Comment object but don't save to database yet
    #         new_review = review_form.save(commit=False)
    #         # Assign the current post to the comment
    #         new_review.Product = product
    #         new_review.author = request.user
    #         # Save the comment to the database
    #         new_review.save()
    # else:
    #     review_form = ReviewForm()
    # 'review_form': review_form
    recommends = None
    if check_parent_or_children(product):
        if request.user.is_superuser:
            recommends = ProductRecommendations.objects.filter(parent_id=product.pk)
        else:
            recommends = ProductRecommendations.objects.filter(Q(parent_id=product.pk) & Q(parent__active=True))
        recommends = [{'name': i.childer.name, 'url': i.childer.get_absolute_url,'img':i.childer.get_image_main,'active':i.childer.active}for i in recommends]

    else:
        if request.user.is_superuser:
            recommends = ProductRecommendations.objects.filter(childer_id=product.pk)
        else:
            recommends = ProductRecommendations.objects.filter(Q(childer_id=product.pk) & Q(childer__active=True))

        recommends = [{'name': i.parent.name, 'url': i.parent.get_absolute_url,'img':i.parent.get_image_main,'active':i.parent.active} for i in recommends]
    # abc = [i for i in accessories]
    # print(abc)
    # recommends = [{'name':'test_1','url':'lalalal'},{'name':'test_1','url':'lalalal'},{'name':'test_1','url':'lalalal'},
    #               {'name':'test_1','url':'lalalal'},{'name':'test_1','url':'lalalal'},]
    print('*'*8)
    print(recommends)
    print('*' * 8)
    if request.user.is_authenticated:
        try:
            rating_product = Rating.objects.get(product__id=pk,user=request.user).value
        except Rating.DoesNotExist:
            rating_product = 0
    else:
        rating_product = 0
        print(type(rating_product))
        # print(type(rating_product))
        # print('---')
        # print(product.get_sale)
        # print('---')
        # for item in rating_product:
        #     if item.get('value') is not None:
        #         rating_p = item.get('value')
        # print(rating_p)
        # print(rating_product)


    p_test = Product.objects.all().annotate(avg=Avg('ratings')).order_by('avg')
    print('рейтинг:')
    print(p_test)
    # print(product_img)
    # s_p = str(product.id)
    # NEWS_COUNT_PER_PAGE = 2
    # page = int(request.GET.get('page', 1))
    # p = paginator.Paginator(reviews,
    #                         2)
    # try:
    #     review_page = p.page(page)
    # except paginator.EmptyPage:
    #     review_page = paginator.Page([], page, p)
    # if not request.is_ajax():
    return render(request, 'product_detail.html',
                      {'product': product,
                       # 'sp': s_p,
                       'review_form': review_form,
                       'rating_product': rating_product,
                       'check_fav': check_fav,
                       'recommends': recommends
                       })
    # else:
    #     content = ''
    #     for review in review_page:
    #         content += render_to_string('review-item.html',
    #                                     {'review': review},
    #                                     request=request)
    #     return JsonResponse({
    #         "content": content,
    #         "end_pagination": True if page >= p.num_pages else False,
    #     })





def del_review(request):
    """Функция добавления комментария"""
    if request.method == "POST":
        temp = json.load(request)
        review = Review.objects.filter(product_id=temp.get('product_id'),id=temp.get('rew_id'))
        review.delete()
        return HttpResponse('ok')


def add_review(request):
    """Функция удаления комментария"""
    # temp = json.load(request)
    # product = get_object_or_404(Product, pk=temp['product_id'])
    tz = get_localzone()  # local timezone
    d = datetime.today().strftime("%d-%b-%Y %H:%M")
    author = request.user
    if request.method == "POST":
        print(request.POST)
        form = ReviewForm(request.POST)
        product = Product.objects.get(id=int(request.POST.get("product_id")))
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.product = product
            form.author = author
            form.save()
            print(form.text)
        return JsonResponse(
                dict(author=str(author),
                     date=d,
                     text=form.text,
                     ))

        # if len(temp['txt_rew']) > 0:
        #     print(temp['txt_rew'])
        #     res = Review(text=temp['txt_rew'], product=product, author=request.user)
        #     if temp.get("parent", None):
        #         res.parent_id = int(request.POST.get("parent"))
        #     res.save()
        # if temp['change'] == 'del':
        #     review = Review.objects.get(id = temp['review_id'])
        #     review.delete()



def add_rating(request):
    """Функция добавления рейтинга"""
    if request.method == 'POST':
        data = json.load(request)
        product = get_object_or_404(
            Product,
            pk=data.get('product_id'))
        Rating.objects.update_or_create(
            product=product,
            user=request.user,
            defaults={"value": data.get('itemValue')})
        return HttpResponse('Спасибо за оценку')




class ProductListView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'product_list.html'


# class SearchResultsListView(LoginRequiredMixin,ListView):
#     model = Product
#     paginate_by = '3'
#     context_object_name = 'product_list'
#     template_name = 'search_results.html'
#     login_url = 'account_login'
#
#     # paginator = Paginator(products, 2)
#     # page_number = request.GET.get('page')
#     # page_obj = paginator.get_page(page_number)
#
#     def get_queryset(self):
#         query = self.request.GET.get('q', None)
#         print(query)
#         return Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)
#                                       | Q(category__name__icontains=query))

def search_result(request):
    """Функция поиска по сайту"""
    if request.user.is_superuser:
        products_list = Product.objects.all()
    else:
        products_list = Product.products_is_user.get_users()
    query = request.GET.get('q')
    if query:
        products_list = products_list.filter(Q(name__icontains=query) | Q(description__icontains=query)
                                      | Q(category__name__icontains=query))
    paginator = Paginator(products_list, 3) # 6 posts per page
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products
    }
    return render(request, "search_results.html", context)




def show_category_detail(request, id,slug):
    """Функция отображения продуктов выбранной категории + сортировка по выбранному фильтру"""
    category = get_object_or_404(Category, id=id, slug=slug)
    form = ChoiceSort()
    if request.user.is_superuser:
        products = Product.objects.filter(category_id=id)
    else:
        products = Product.products_is_user.get_users().filter(category_id=id)
    error = ''
    if request.method == 'POST':
        form = ChoiceSort(request.POST)
        if request.POST["filter_form_val"] == 'empty':
            error = 'Ошибка, Вы не выбрали фильтр!!!'
        elif request.POST["filter_form_val"] == 'avg':
            # products = Product.objects.filter(Q(category_id=id) & Q(active=True)).annotate(avg=Avg('ratings__value'))
            products = products.annotate(avg=Avg('ratings__value'))
            print(products)
            # for product in products:
            #     if product.avg is None:
            #         product.avg = 0.0
            #     print(product.avg)

            products = products.annotate(avg=Case(When(avg=None,then=Value(0.0)), default=Avg('ratings__value'))).order_by('-avg')
            for product in products:
                print(product.avg)
            # products.order_by('-avg')

        elif request.POST["filter_form_val"] == 'reviews_count':
            # products = Product.objects.filter(Q(category_id=id) & Q(active=True)).annotate(cnt=Count('reviews')).order_by('-cnt')
            products = products.annotate(cnt=Count('reviews')).order_by('-cnt')
            print(products)
        elif request.POST["filter_form_val"] == 'popular':
            # products = Product.objects.filter(Q(category_id=id) & Q(active=True)).annotate(cnt=Count('order_items')).order_by('-cnt')
            products = products.annotate(cnt=Count('order_items')).order_by('-cnt')
            print(products)
        else:
            products = products.order_by(request.POST["filter_form_val"])

    # paginator = Paginator(products, 2)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    return render(request,'category_detail.html',{'category':category,'products':products,'form':form,'error':error})



# def filter_p(filtr,id):
#     products = Product.objects.filter(category_id=id).order_by(filtr).values('id','price','name')
#     return list(products)


# def filter_category(request):
#     if request.method == 'POST':
#         temp = json.load(request)
#         print(temp)
#         filtr = temp['form_filter']
#         id = temp['category_id']
#         products = filter_p(filtr,id)
#         paginator = Paginator(products, 2)
#         page_number = request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         html = render_to_string('products_filter.html', {'page_obj': page_obj})
#         print(html)
#         return HttpResponse(html)


        # category = Category.objects.get(pk=id)
        # form = ChoiceSort()
        # products = Product.objects.filter(category_id=id)
        # if request.method == 'POST':
        #     form = ChoiceSort(request.POST)
        #     filtr = request.POST['sortirovrka']
        #     if filtr == 'min_price':
        #         products = Product.objects.filter(category_id=id).order_by('price').values()
        #     if filtr == 'max_price':
        #         products = Product.objects.filter(category_id=id).order_by('-price').values()
        #     if filtr == 'max_date':
        #         products = Product.objects.filter(category_id=id).order_by('-created').values()
        #     if filtr == 'min_date':
        #         products = Product.objects.filter(category_id=id).order_by('created').values()




class CategoryListView(ListView):
    """Функция отображения всех категорий"""
    model = Category
    context_object_name = 'category_list'
    template_name = 'category_list.html'


# class AddStarRating(View):
#     """Добавление рейтинга товара"""
#     def get_client_ip(self, request):
#         x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#         if x_forwarded_for:
#             ip = x_forwarded_for.split(',')[0]
#         else:
#             ip = request.META.get('REMOTE_ADDR')
#         return ip
#
#     def post(self, request):
#         form = RatingForm(request.POST)
#         print(request.POST)
#         print(RatingStar.objects.all())
#         if form.is_valid():
#             Rating.objects.update_or_create(
#                 ip=self.get_client_ip(request),
#                 product_id=int(request.POST.get("product")),
#                 defaults={'star_id': int(request.POST.get("star"))}
#             )
#             avg_stat = Rating.objects.filter(product__id=int(request.POST.get("product"))).aggregate(Avg('star'))
#             return JsonResponse(avg_stat)









        # if request.method == "POST":
        #     print(request.POST)
        #     form = ReviewForm(request.POST)
        #     product = Product.objects.get(id=int(request.POST.get("product_id")))
        #     if form.is_valid():
        #         form = form.save(commit=False)
        #         if request.POST.get("parent", None):
        #             form.parent_id = int(request.POST.get("parent"))
        #         form.product = product
        #         form.author = author
        #         form.save()
        #         print(form.text)
        #     return JsonResponse(
        #             dict(author=str(author),
        #                  date=d.strftime("%d-%b-%Y %H:%M"),
        #                  text=form.text,
        #                  ))

