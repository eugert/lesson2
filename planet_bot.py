
# Установите модуль ephem
# Добавьте в бота команду /planet, которая будет принимать на вход название планеты на английском.
# При помощи условного оператора if и ephem.constellation научите бота отвечать, 
# в каком созвездии сегодня находится планета.

# Импортируем компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import datetime
import ephem


# Настройки прокси
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}
# Настройка логирования
import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


# Функция будет вызываться, когда пользователь в чате напишет /start вручную или подключится к боту в первый раз
def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


# Ответы о планетах
def talk_about_planet(bot, update):
    user_text = update.message.text 
    
    planet = user_text.capitalize()
    print ('Вопрос о планете ' + planet)

    if planet=='Sun':
        place=ephem.constellation(ephem.Sun(datetime.datetime.now()))
    elif planet=='Moon':
        place=ephem.constellation(ephem.Moon(datetime.datetime.now()))
    elif planet=='Earth':
        place=ephem.constellation(ephem.Earth(datetime.datetime.now()))
    elif planet=='Mercury':
        place=ephem.constellation(ephem.Mercury(datetime.datetime.now()))
    elif planet=='Mars':
        place=ephem.constellation(ephem.Mars(datetime.datetime.now()))
    elif planet=='Venus':
        place=ephem.constellation(ephem.Venus(datetime.datetime.now()))
    elif planet=='Jupiter':
        place=ephem.constellation(ephem.Jupiter(datetime.datetime.now()))
    elif planet=='Uranus':
        place=ephem.constellation(ephem.Uranus(datetime.datetime.now()))
    elif planet=='Neptune':
        place=ephem.constellation(ephem.Neptune(datetime.datetime.now()))
    else:
        place = 'NO'

    print (place)
    if place == 'NO':
        answer_text = 'Не могу дать ответ'
    else:
        answer_text = planet +' находится в '+ place[1]
    
    print (answer_text)
    update.message.reply_text(answer_text)


# Функция, которая соединяется с платформой Telegram, "тело" бота
def main():
    mybot = Updater("581633010:AAFJin9MwlMm_cB91QEmbvfKzZPL18dUYcE", request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_about_planet))

    mybot.start_polling()
    mybot.idle()


# Вызываем функцию - эта строчка собственно запускает бота
main()
