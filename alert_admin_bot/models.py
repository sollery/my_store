from django.db import models

# Create your models here.


class SettingsAlertBot(models.Model):
    alert_bot_token = models.CharField(max_length=200,verbose_name='Токен')
    alert_bot_chat_id = models.CharField(max_length=200, verbose_name='Айди чата')
    alert_bot_text_message = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.alert_bot_chat_id

    class Meta:
        verbose_name = 'Оповещение'
        verbose_name_plural = 'Оповещения'