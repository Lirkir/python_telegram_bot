import time
import json
import requests
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

API_URL = 'https://api.chucknorris.io/jokes/'
bot = telepot.Bot('410868942:AAH1a1oLRNJz1e1DYJKsA2b2duhIl7WwJv4') 

def on_chat_message(msg):    
    content_type, _, chat_id = telepot.glance(msg)  # glance возвращает массив нужных данных. Пытается распарсить сообщенеи в чате

    if content_type != 'text': #   Если прислали аудио или фото, просит прислать текст
        bot.sendMessage(chat_id, 'Give me the text. Woof')
        return

    command = msg['text'].strip().lower()[1:] # Убираем пробелы (strip()), в нижний регистр и удаляем "/"

    if command == 'random':
        req = requests.get('https://api.chucknorris.io/jokes/random')  # Забираем шутку
        joke = req.json()
        bot.sendMessage(chat_id, joke['value'])
    elif command == 'joke':
        req = requests.get('https://api.chucknorris.io/jokes/categories')  # Забираем категории
        categories = req.json()
        keyboard = list(map(lambda name: [InlineKeyboardButton(text=name, callback_data=name)], categories)) # Мапаем полученные категории в массив типа InlineKeyboardButton, так как InlineKeyboardMarkup принимает такую структуру 
                                                        # InlieKeyboardButton имеет при себе text (текст кнопки) и callback_data - данные, которые отправяться на бот на обработку при нажатии кнопки под сообщением (это в итоге прилетит в on_calback_query)

        markup = InlineKeyboardMarkup(inline_keyboard=keyboard) 
        bot.sendMessage(chat_id, 'Select a category', reply_markup=markup) # отсылаем сообщение в чат с inline-клавиатурой
    else:
        bot.sendMessage(chat_id, 'Woof?') # Если сообщение не несет команду, выдаем это сообщение и ничего не делаем

def on_callback_query(msg):  # парсим с помощью glance
    query_id, _, data = telepot.glance(msg, flavor='callback_query')  # flavor указываем, чтобы другие типы сообщения парсить
    # В data лежит то, что положили еще у InlineKeyboardButton в callback_data, то есть просто имя нашей категории, такое же как и название у кнопки
    req = requests.get('https://api.chucknorris.io/jokes/random?category=' + data) # На этот раз обращаемся к api с уже конкретной категорией
    joke = req.json()

    msg_idf = telepot.message_identifier(msg['message']) # Получаем идентификатор сообщения. Принимает на вход объект Message. 
            # В ключе message лежит сообщение, с которого пришел callback, то есть то сообщение, под которым находятся эти кнопки
    bot.answerCallbackQuery(query_id) # Вызываем, чтобы бот понял, что мы обработали callback (нажали на категорию)
    bot.editMessageText(msg_idf, joke['value']) # Меняем сообщение, чтобы заменил категории на шутку и убрал кнопки



MessageLoop(bot, {             # Регулярно ходит к api и проверяет новые сообщения
                               # Каждое сообщение, зависимости от его типа, отправляет на обработку
    'chat': on_chat_message,   # обычное сообщение
    'callback_query': on_callback_query  # callback (категории, прикрепленны к сообщению)
}).run_as_thread()

while 1:
    time.sleep(10)
