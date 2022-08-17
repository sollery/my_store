from django import forms
from .models import Review
SORT_CHOICES = [
    ('min_price', 'Мин цена'),
    ('max_price', 'Макс цена'),
    ('min_date', 'Мин дата'),
    ('max_date', 'Макс дата'),
    ]

class ChoiceSort(forms.Form):
    sortirovrka = forms.CharField(label='Как отсортировать',
                                     widget=forms.RadioSelect(choices=SORT_CHOICES))


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('review',)

