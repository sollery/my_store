from django import forms
from .models import Review, Product, ProductImage, Category, CategoryImage

SORT_CHOICES = [
    ('empty','Выберите фильтр'),
    ('price', 'по возрастанию цен'),
    ('-price', 'по убыванию цен'),
    ('created', 'старые товары'),
    ('-created', 'новый товары'),
    ('avg', 'по рейтингу'),
    ('reviews_count','по кол-ву отзывов')
    ]

# rating_stars = [
#     ('5', 'RatingStar'),
#     ('4', 'RatingStar'),
#     ('3', 'RatingStar'),
#     ('2', 'RatingStar'),
#     ('1', 'RatingStar'),
#     ]


class ChoiceSort(forms.Form):
    filter_form_val = forms.CharField(label='Как отсортировать', widget=forms.Select(choices=SORT_CHOICES))

    def __init__(self, *args, **kwargs):
        super(ChoiceSort, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text',)

# class RatingForm(forms.ModelForm):
#     """Форма добавления рейтинга"""
#     star = forms.ModelChoiceField(
#         queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
#     )
#
#
#     class Meta:
#         model = Rating
#         fields = ("star",)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category','name','slug','description','price')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class ProductImgForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ('image', 'main')

    def __init__(self, *args, **kwargs):
        super(ProductImgForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name','slug')

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class CategoryImgForm(forms.ModelForm):
    class Meta:
        model = CategoryImage
        fields = ('image',)

    def __init__(self, *args, **kwargs):
        super(CategoryImgForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
