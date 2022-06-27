from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import Permission
from accounts.models import CustomUser


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


