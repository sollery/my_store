
import json
from datetime import datetime

from django.core import paginator
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from tzlocal import get_localzone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
# Create your views here.
from django.views.generic import DetailView, ListView
from .forms import ChoiceSort,ReviewForm
from shop.models import Product, Category,Review




def product_detail(request, pk, slug):
    # reviews = Review.objects.filter(Product_id=pk)
    # print(reviews)
    product = get_object_or_404(Product, id=pk, slug=slug)
    reviews = product.reviews.filter(active=True)
    review_form = ReviewForm()
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
                       'cart_product_form': cart_product_form, 'sp': s_p, 'reviews': review_page, 'review_form': review_form

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
        return JsonResponse(dict(author=str(author), date=d.strftime("%d-%b-%Y %H:%M")))




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
    if request.method == 'POST':
        form = ChoiceSort(request.POST)
        b = request.POST['sortirovrka']
        if b == 'min_price':
            products = Product.objects.filter(category_id=id).order_by('price')
        if b == 'max_price':
            products = Product.objects.filter(category_id=id).order_by('-price')
        if b == 'max_date':
            products = Product.objects.filter(category_id=id).order_by('-created')
        if b == 'min_date':
            products = Product.objects.filter(category_id=id).order_by('created')
    return render(request,'category_detail.html',{'category':category,'products':products,'form':form})


class CategoryListView(ListView):
    model = Category
    context_object_name = 'category_list'
    template_name = 'category_list.html'


