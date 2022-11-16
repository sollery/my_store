


from django.core.management.base import BaseCommand
from django.conf import settings
from shop.models import Product,ProductImage,Category,CategoryImage
from orders.models import Order
from telebot import TeleBot, types

# Объявление переменной бота
bot = TeleBot(settings.TELEGRAM_BOT_API_KEY)
chat_id = 835866403
markup = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton(text="Старт",callback_data='Старт')
markup.add(btn1)
bot.send_message(chat_id, text='Нажмите на кнопку старт', reply_markup=markup)
# Название класса обязательно - "Command"
class Command(BaseCommand):
    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2) # Сохранение обработчиков
        bot.load_next_step_handlers()# Загрузка обработчиков
        bot.infinity_polling()


# def check_info(code):
#     code = code.replace('/info ', '')
#     order = None
#     try:
#         order = Order.objects.get(code=code)
#     except Order.DoesNotExist:
#         pass
#     if order is None:
#         return False
#     return True

@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback(callback):
    if callback.data == 'Старт':
        # markup = types.InlineKeyboardMarkup()
        # # btn1 = types.InlineKeyboardButton(text="Информация о заказе")
        # btn2 = types.InlineKeyboardButton(text="Пока",callback_data='Пока')
        # btn3 = types.InlineKeyboardButton(text='ссылка на сайт',url='http://127.0.0.1:8000/')
        # # btn4 = types.InlineKeyboardButton(text="/products")
        # btn5 = types.InlineKeyboardButton(text="Категории",callback_data='Категории')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
        btn2 = types.KeyboardButton(text='ссылка на сайт')
        btn3 = types.KeyboardButton(text="Категории")
        btn4 = types.KeyboardButton(text="Обратная связь")
        btn1 = types.KeyboardButton(text="Пока")
        markup.add(btn1, btn2, btn3, btn4)
        # markup.add(btn1, btn2, btn3, btn4, btn5,)
        bot.send_message(callback.message.chat.id,
                         "Привет, {0.first_name}!".format(callback.from_user),reply_markup=markup)
        bot.send_sticker(callback.message.chat.id,"CAACAgIAAxkBAAEV7fRizoJdJUEQNtJ6Gp_zbs4_th8mGwACgA8AAph0iEsEu1XOvtkOmSkE")
        print(callback)

@bot.message_handler(commands=['products'])
def get_products(message):
    products = Product.objects.all()
    bot.send_message(message.chat.id, text='Список продуктов на сайте')
    for i in products:
        file = open(f"C:/proj_z/store/media/{ProductImage.image_main_objects.get(product_id=i.pk)}",'rb')
        bot.send_photo(message.chat.id,file,i.name)


# @bot.callback_query_handler(func= lambda callback: callback.data)
# def check_callback(callback):
#     # bot.send_message(message.chat.id, text='Список продуктов на сайте')
#     if callback.data == 'Пока':
#         bot.send_message(callback.message.chat.id,text='Пока {}, возвращайся!'.format(callback.message.chat.first_name))
#         print(callback.message)
#     if callback.data == 'Категории':
#         categories = Category.objects.all()
#         for i in categories:
#             file = open(f"C:/proj_z/store/media/{CategoryImage.objects.get(category_id=i.pk)}", 'rb')
#             print(CategoryImage.objects.get(category_id=i.pk))
#             bot.send_photo(callback.message.chat.id, file)
#             bot.send_message(callback.message.chat.id,f'[{i.name}](http://127.0.0.1:8000{i.get_absolute_url()})',parse_mode='Markdown')
@bot.message_handler(content_types=['text'])
def check_message(message):
    # bot.send_message(message.chat.id, text='Список продуктов на сайте')
    if message.text == 'Пока':
        bot.send_message(message.chat.id,text='Пока {}, возвращайся!'.format(message.chat.first_name))
    elif message.text== 'Категории':
        categories = Category.objects.all()
        for i in categories:
            file = open(f"C:/proj_z/store/media/{CategoryImage.objects.get(category_id=i.pk)}", 'rb')
            print(CategoryImage.objects.get(category_id=i.pk))
            bot.send_photo(message.chat.id, file)
            bot.send_message(message.chat.id,f'[{i.name}](http://127.0.0.1:8000{i.get_absolute_url()})',parse_mode='Markdown')
    elif message.text == 'ссылка на сайт':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='ссылка на сайт',url='http://127.0.0.1:8000/')
        # bot.send_message(message.chat.id,'[перейти](http://127.0.0.1:8000)',parse_mode='Markdown')
        markup.add(btn1)
        bot.send_message(message.chat.id, text='перейти на сайт', reply_markup=markup)
    elif message.text == 'Обратная связь':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='обратная связь', url='http://127.0.0.1:8000/shop/message_from_user_create/')
        # bot.send_message(message.chat.id,'[перейти](http://127.0.0.1:8000)',parse_mode='Markdown')
        markup.add(btn1)
        bot.send_message(message.chat.id, text='написать', reply_markup=markup)

    else:
        bot.send_message(message.chat.id,'не понимаю')
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Старт", callback_data='Старт')
        markup.add(btn1)
        bot.send_message(chat_id, text='Нажмите на кнопку старт, чтобы узнать о возможностях', reply_markup=markup)





# @bot.message_handler(commands=['info'])
# def products(message):
#     products = Product.objects.all()
#     print(products)
#     products = [i.name for i in products]
#     bot.send_message(message.chat.id,",".join(products))


# @bot.message_handler(content_types=['text'])
# def func(message):
#     if message.text == 'Информация о заказе':
#         bot.send_message(message.chat.id, text= 'Чтобы узнать информацию о вашем заказе, напишите /info и code (/info code)')
#         bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAEV7ehizoF94Df7bLIH6MW1dSexciccWgAChg0AAhPBgUghuXGJoyruzSkE")
#     elif '/info' in message.text and check_info(message.text):
#         bot.send_message(message.chat.id,'{}, {}'.format(message.from_user.first_name, 'Такой заказ есть'))
#     elif message.text.capitalize() == 'Пока-пока' or message.text.capitalize() == 'Пока':
#         bot.send_message(message.chat.id,
#                          text='Пока {}, возвращайся!'.format(message.from_user.first_name))
#         bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEV7dFizn-dGrpeN_2-D4uZsaIvhQ1qMAACZwsAAvaEYUuPBEudOdF6oikE")
#     elif message.text == 'ссылка на сайт':
#         bot.send_message(message.chat.id, 'Заходите к нам на сайт! http://127.0.0.1:8000/')
#     else:
#         bot.send_message(message.chat.id,text='Такого заказа нет')
#         bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEV7j9izo3WVlHh59Cw4xbgycgzu_5AHQAC1QoAAtesYUvHcC3ZlShALSkE")
# @bot.message_handler(chat_types=['private'],func= lambda x: x.text.capitalize() == 'Категории')
# def get_categories(message):
#     categories = Category.objects.all()
#     for i in categories:
#         bot.send_message(message.chat.id, i.name)