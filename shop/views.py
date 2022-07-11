from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
# Create your views here.
from django.views.generic import DetailView, ListView
from cart.cart import Cart
from shop.models import Product, Category,Review


def product_detail(request, pk, slug):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    print(session_key)
    product = get_object_or_404(Product, id=pk, slug=slug)
    # if request.method == 'POST':
    #     cart = Cart(request)
    #     print(cart.session)
    #     form = CartAddProductForm(request.POST)
    #     if form.is_valid():
    #         cd = form.cleaned_data
    #         print(cd['quantity'])
    #         cart.add(product=product,quantity=cd['quantity'],update_quantity=cd['update'])
    #     print('1')
    # reviews = Review.objects.filter(Product_id=pk)
    # print(reviews)
    # # product = get_object_or_404(Product, id=pk, slug=slug)
    cart_product_form = CartAddProductForm()
    return render(request, 'product_detail.html',
    {'product': product,
    'cart_product_form': cart_product_form})



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


def show_category_detail(request,id):
    category = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)
    return render(request,'category_detail.html',{'category':category,'products':products})


class CategoryListView(ListView):
    model = Category
    context_object_name = 'category_list'
    template_name = 'category_list.html'


