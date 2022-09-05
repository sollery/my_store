from django.urls import path
from . import views
urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('data_cart/', views.data_cart, name='data_cart'),
    path('cart_clear/', views.cart_clear, name='cart_clear'),
    # path('add/<int:id>/', views.cart_add, name='cart_add'),
    # path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]