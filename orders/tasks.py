import celery
from django.core.mail import send_mail
from store.celery import app
from .models import Order



