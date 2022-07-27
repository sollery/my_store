from django.urls import path
from . import views
urlpatterns = [
    path('', views.cart_change, name='cart_detail'),
    path('add/<int:id>/', views.cart_add, name='cart_add'),
    # path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]