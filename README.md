# python_telegram_bot
Бот для любителей Чака Норриса. Выдает шутливые факты.
Используется api.chucknorris.io - api.chucknorris.io

Бот имеет две команды:
/random – выдает случайный факт о Чаке Норрисе. 
/joke – выдает категории фактов на выбор


Создание бота.
В Telegram написать BotFather. /n
/newbot – создание нового бота /n
Написать имя бота в виде (название)_bot /n
/token – получение токена  /n
После последней команды набрать имя бота, к которому необходим токен. /n
Бот создан.

На сервер необходимо загрузить файл для бота.
Обязательно указать токен для работы бота в файле:
bot = telepot.Bot('токен_бота')



Документация
Telefram Bot API - core.telegram.org/bots/api
InlineKeyboardMarkup — core.telegram.org/bots/api#inlinekeyboardmarkup 
CallbackQuery - core.telegram.org/bots/api#callbackquery
Telepot. Introduction - telepot.readthedocs.io/en/latest/index.html
