from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.contrib.sessions.models import Session

class CustomUser(AbstractUser):

    class Meta:
        db_table = 'CustomUser'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
# Create your models here.



class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    session = models.ForeignKey(Session,models.CASCADE)