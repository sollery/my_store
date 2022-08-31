from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Category,Favorites


def get_caterogy_list(request):
    category_list = Category.objects.all()
    return {'category_list':category_list}

#


def get_favorites(request):
    user = request.user
    if request.user.is_authenticated:
        favorites = Favorites.objects.filter(user=user)
        return {'favorites': favorites}
    else:
        return {'user': user}




