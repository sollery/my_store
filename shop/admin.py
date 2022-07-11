from django.contrib import admin
from .models import Category, Product, Review, ProductImage


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


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

class ProductImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage

admin.site.register(ProductImage, ProductImageAdmin)