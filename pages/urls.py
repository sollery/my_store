from django.urls import path

from . import views
from .views import *

urlpatterns = [
      path('', views.home, name='home'),
      path('about/', AboutPageView.as_view(), name='about'),
]