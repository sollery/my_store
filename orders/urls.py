from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
        path('', views.order_create, name='order_create'),
        # path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
        # path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),
        path('admin/order/<int:order_id>/pdf/',views.admin_order_pdf,name='admin_order_pdf'),
        path('created_order/<int:order_id>/',views.created_order,name='created_order'),
        path('proof_of_payment_page/<int:order_id>/',views.proof_of_payment_page,name='proof_of_payment_page'),
        # path('proof_of_payment/', views.proof_of_payment,name='proof_of_payment'),
]