from django import forms
from django.core.exceptions import ValidationError
from shop.models import Product, ProductImage, Category, CategoryImage, MessageFromUser, MessageAnswerForUser


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'name', 'slug','description','price')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['category'].empty_label = "Выберите категорию"


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


class MessageForUserForm(forms.ModelForm):
    class Meta:
        model = MessageFromUser
        fields = ('title','email', 'text',)


class MessageAnswerForUserForm(forms.ModelForm):
    class Meta:
        model = MessageAnswerForUser
        fields = ('text',)



class CheckStatusOrder(forms.Form):
    email = forms.EmailField(max_length=255,label='Почта')
    number = forms.IntegerField(min_value=1,label='Номер заказа')

    def __init__(self, *args, **kwargs):
        super(CheckStatusOrder, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'check_inp'

    def clean_number(self):
        number = self.cleaned_data['number']
        if int(number) < 1:
            raise ValidationError('Номер не может быть, отрицательным')