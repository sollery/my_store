from django.urls import path

from . import views
from .views import *

urlpatterns = [
      path('', views.main_shop, name='main_img'),
      path('main/',views.home, name='home'),
      path('about/', AboutPageView.as_view(), name='about'),
      path('favorites/',views.check_favorites,name='favorites'),
      path('change_favorites/',views.change_favorites,name='change_favorites'),
      path('panel/',views.panel,name='panel'),
      path('check_status_order/',views.check_status_order,name='check_status_order'),
      path('status_data/',views.status_data,name='status_data'),
      path('orders_list/',views.orders_list,name='orders_list'),
      path('order_detail/<int:id>/',views.order_detail,name='order_detail'),
      path('message_from_user_create/', views.create_message_from_user, name='create_message_from_user'),
      path('message_list/', views.user_message_list, name='message_list'),
      path('message_detail/<int:pk>/', views.user_message_detail, name='message_detail'),
      path('message_answer/<int:pk>/', views.create_answer_message_for_user, name='message_answer'),
      path('create_product/', views.create_product, name='create_product'),
      path('create_category/', views.create_category, name='create_category'),
      path('product_edit/<int:pk>/',ProductUpdateView.as_view(), name='product_edit'),
      path('upl_img_product/<int:pk>/', views.upl_img_product, name='upl_img_product'),
      path('upl_img_category/<int:pk>/', views.upl_img_category, name='upl_img_category'),
]

