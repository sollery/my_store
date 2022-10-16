from django.contrib import admin
from django.urls import reverse

from django.utils.safestring import mark_safe

from .models import Order, OrderItem, PaymentMethod,DeliveryMethod


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'city', 'paid',
                    'created', 'updated','order_pdf']
    list_filter = ['paid', 'created', 'updated']

    inlines = [OrderItemInline]



@admin.register(PaymentMethod)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(DeliveryMethod)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','price_delivery']


admin.site.register(Order, OrderAdmin)
# Register your models here.
