from django.db import models
from django.db.models import Q
from django.utils import timezone


class DiscountActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(Q(start__lte=timezone.now()) & Q(end__gte=timezone.now()) & Q(active=True))



