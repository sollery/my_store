from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
        path('', views.order_create, name='order_create'),
        path('created_order/<int:order_id>/',views.created_order,name='created_order'),
        path('proof_of_payment_page/<int:order_id>/',views.proof_of_payment_page,name='proof_of_payment_page'),
]