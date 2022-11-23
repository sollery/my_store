from django.contrib import admin
from .models import Category, Product, Review, ProductImage, Rating, Discount, Discount_product, Favorites, \
    CategoryImage, ProductRecommendations, MessageFromUser, MessageAnswerForUser


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'product', 'created_rew', 'active')
    list_filter = ('active', 'created_rew', 'updated_rew')
    search_fields = ('author', 'body')
admin.site.register(Review, ReviewAdmin)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name',  'price', 'created', 'updated','end_price','active']
    list_filter = ['created', 'updated','active']
    list_editable = ['price','active']
    prepopulated_fields = {'slug': ('name',)}


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

class ProductImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage

admin.site.register(ProductImage, ProductImageAdmin)

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ("value", "product", "user")

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['value']


@admin.register(Discount_product)
class Discount_productAdmin(admin.ModelAdmin):
    list_display = ['product','discount','start','end']
# @admin.register(RatingStar)
# class RatingStarAdmin(admin.ModelAdmin):
#     model = RatingStar


@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    list_display = ['product','user']


@admin.register(ProductRecommendations)
class ProductRecommendations(admin.ModelAdmin):
    list_display = ['parent','childer']


class CategoryImageInline(admin.TabularInline):
    model = CategoryImage
    extra = 0


class CategoryImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in CategoryImage._meta.fields]

    class Meta:
        model = CategoryImage


admin.site.register(CategoryImage, CategoryImageAdmin)


@admin.register(MessageFromUser)
class MessageFromUserAdmin(admin.ModelAdmin):
    list_display = ['title','email','text','created','status']

@admin.register(MessageAnswerForUser)
class MessageAnswerForUserAdmin(admin.ModelAdmin):
    list_display = ['text', 'created']
