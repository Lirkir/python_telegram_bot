# python_telegram_bot
Бот для любителей Чака Норриса. Выдает шутливые факты.
Используется api.chucknorris.io - api.chucknorris.io

Бот имеет две команды:

/random – выдает случайный факт о Чаке Норрисе. 

/joke – выдает категории фактов на выбор


# Создание бота.
В Telegram написать BotFather. 

/newbot – создание нового бота 

Написать имя бота в виде (название)_bot 

/token – получение токена  

После последней команды набрать имя бота, к которому необходим токен. 

Бот создан, токен получен.

Установить на сервер telepot:

$ pip install telepot

$ pip install telepot --upgrade


На сервер необходимо загрузить файл для бота.

Обязательно указать токен для работы бота в файле:

bot = telepot.Bot('токен_бота')



# Документация
Telegram Bot API - core.telegram.org/bots/api

Telepot. Introduction - telepot.readthedocs.io/en/latest/index.html

InlineKeyboardMarkup — core.telegram.org/bots/api#inlinekeyboardmarkup 

CallbackQuery - core.telegram.org/bots/api#callbackquery

