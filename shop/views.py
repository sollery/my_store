
import json
from datetime import datetime

from django.core import paginator
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.views import View
from tzlocal import get_localzone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Avg
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
# Create your views here.
from django.views.generic import DetailView, ListView
from .forms import ChoiceSort, ReviewForm
from shop.models import Product, Category, Review, ProductImage, Rating


def product_detail(request, pk, slug):
    # reviews = Review.objects.filter(Product_id=pk)
    # print(reviews)
    product = get_object_or_404(Product, id=pk, slug=slug)
    reviews = product.reviews.filter(active=True)
    print(reviews)
    review_form = ReviewForm()

    # product_img=ProductImage.objects.filter(product_id=pk,is_main=True)
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
    avg_stat = Rating.objects.filter(product__id=pk).aggregate(Avg('value')).get('value__avg')
    print(avg_stat)
    rating_product = Rating.objects.filter(product__id=pk,user=request.user).values('value')

    print(type(rating_product))
    rating_p = 0
    for item in rating_product:
        if item.get('value') is not None:
            rating_p = item.get('value')
    print(rating_p)
    print(rating_product)

    # print(product_img)
    s_p = str(product.id)
    cart_product_form = CartAddProductForm()
    NEWS_COUNT_PER_PAGE = 2
    page = int(request.GET.get('page', 1))
    p = paginator.Paginator(reviews,
                            2)
    try:
        review_page = p.page(page)
    except paginator.EmptyPage:
        review_page = paginator.Page([], page, p)
    if not request.is_ajax():
        return render(request, 'product_detail.html',
                      {'product': product,
                       'cart_product_form': cart_product_form,
                       'sp': s_p,
                       'reviews': review_page,
                       'review_form': review_form,'rating_product':rating_product,
                       'rating_p': rating_p,
                       'avg_stat': avg_stat
                       })
    else:
        content = ''
        for review in review_page:
            content += render_to_string('review-item.html',
                                        {'review': review},
                                        request=request)
        return JsonResponse({
            "content": content,
            "end_pagination": True if page >= p.num_pages else False,
        })


def add_review(request):
    if request.method == 'POST':
        temp = json.load(request)
        product = get_object_or_404(Product, pk=temp['product_id'])
        tz = get_localzone()  # local timezone
        d = datetime.now(tz)
        author = request.user
        if temp['change'] == 'add':
            if len(temp['txt_rew']) > 0:
                print(temp['txt_rew'])
                res = Review(review=temp['txt_rew'], Product=product, author=request.user)
                res.save()
        if temp['change'] == 'del':
            review = Review.objects.get(id = temp['review_id'])
            review.delete()
        return JsonResponse(
            dict(author=str(author),
                 date=d.strftime("%d-%b-%Y %H:%M")
                 ))


def add_rating(request):
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


class SearchResultsListView(LoginRequiredMixin,ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'search_results.html'
    login_url = 'account_login'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)
                                      | Q(category__name__icontains=query))


def show_category_detail(request, id):
    category = Category.objects.get(pk=id)
    form = ChoiceSort()
    products = Product.objects.filter(category_id=id)
    return render(request,'category_detail.html',{'category':category,'products':products,'form':form})

def filter_p(filtr,id):
    products = Product.objects.filter(category_id=id).order_by(filtr).values('id','price','name')
    return list(products)


def filter_category(request):
    if request.method == 'POST':
        temp = json.load(request)
        print(temp)
        filtr = temp['form_filter']
        id = temp['category_id']
        products = filter_p(filtr,id)
        # if filtr == 'min_price':
        #     products = Product.objects.filter(category_id=id).order_by('price').values('id','description','price','name')
        # if filtr == 'max_price':
        #     products = Product.objects.filter(category_id=id).order_by('-price').values('id','description','price','name')
        # if filtr == 'max_date':
        #     products = Product.objects.filter(category_id=id).order_by('-created').values('id','description','price','name')
        # if filtr == 'min_date':
        #     products = Product.objects.filter(category_id=id).order_by('created').values('id','description','price','name')
        return JsonResponse({'products':products})



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


