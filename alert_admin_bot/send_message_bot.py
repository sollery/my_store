from .models import SettingsAlertBot
import requests

def send_alert_bot(link,tp):
    if tp == 'Обращение':
        settings_bot = SettingsAlertBot.objects.get(pk=1)
    elif tp == 'Заказ':
        settings_bot = SettingsAlertBot.objects.get(pk=2)
    token = str(settings_bot.alert_bot_token)
    chat_id = str(settings_bot.alert_bot_chat_id)
    text = str(settings_bot.alert_bot_text_message)

    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'
    text_mes = text + link

    req = requests.post(method, data = {'chat_id' : chat_id, 'text': text_mes})



# def send_alert_bot_order(order_link):
#     settings_bot = SettingsAlertBot.objects.get(pk=2)
#     token = str(settings_bot.alert_bot_token)
#     chat_id = str(settings_bot.alert_bot_chat_id)
#     text = str(settings_bot.alert_bot_text_message)
#     api = 'https://api.telegram.org/bot'
#     method = api + token + '/sendMessage'
#     text_mes = text + order_link
#
#     req = requests.post(method, data = {'chat_id' : chat_id, 'text': text_mes})







