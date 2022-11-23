from django import forms
from .models import Review, Product, ProductImage, Category, CategoryImage, MessageFromUser, MessageAnswerForUser

SORT_CHOICES = [
    ('empty','Выберите фильтр сортировки'),
    ('price', 'по возрастанию цены'),
    ('-price', 'по убыванию цены'),
    ('created', 'старые товары'),
    ('-created', 'новые товары'),
    ('avg', 'по рейтингу'),
    ('reviews_count','по кол-ву отзывов'),
    ('popular', 'по популярности')
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


