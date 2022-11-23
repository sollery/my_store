from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductListView, CategoryListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/<slug:slug>/', views.product_detail, name='product_detail'),
    path("add_rating/", views.add_rating, name='add_rating'),
    # path('filter_category/',views.filter_category, name='filter_category'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:id>/<slug:slug>/', views.show_category_detail, name='category_detail'),
    path('search/', views.search_result, name='search_results'),
    path('data_review/', views.add_review, name='data_review'),
    path('del_review/', views.del_review, name='del_review'),


]