from django.contrib import admin
from .models import Category, Product, Review

class ReviewInline(admin.TabularInline):
    model = Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ReviewInline, ]
    list_display = ['name',  'price', 'count', 'created', 'updated']
    list_filter = ['created', 'updated']
    list_editable = ['price', 'count']
    prepopulated_fields = {'slug': ('name',)}



