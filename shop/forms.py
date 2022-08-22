from django import forms
from .models import Review

SORT_CHOICES = [
    ('price', 'Мин цена'),
    ('-price', 'Макс цена'),
    ('created', 'Мин дата'),
    ('-created', 'Макс дата'),
    ]

rating_stars = [
    ('5', 'RatingStar'),
    ('4', 'RatingStar'),
    ('3', 'RatingStar'),
    ('2', 'RatingStar'),
    ('1', 'RatingStar'),
    ]

class ChoiceSort(forms.Form):
    filter_form_val = forms.CharField(label='Как отсортировать',
                                     widget=forms.RadioSelect(choices=SORT_CHOICES))


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('review',)

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