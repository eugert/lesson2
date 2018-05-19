# Импортируем компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import config
import logging

# Настройки прокси
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}
# Настройка логирования

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


# Функция подсчета количества строк
def word_count(bot, update):
    user_text = update.message.text 
    print ('world_count: ', user_text)

    if (user_text.count('"') != 2):
        bot_answer = 'Должны быть две двойных кавычки'
    else:
        chk_text=user_text[user_text.find('"')+1 : user_text.rfind('"')]
        print ('Анализируем: ',chk_text)
        chk_list = chk_text.split(' ')
        print ('Список ', chk_list)
        chk_cont = len(chk_list) - chk_list.count('')
        if chk_cont == 0:
            bot_answer = 'Нет слов'
        else: 
            bot_answer =  'Количество слов {}.'.format(chk_cont)

    print (bot_answer)
    update.message.reply_text(bot_answer)


# Функция, которая соединяется с платформой Telegram, "тело" бота
def main():
        mybot = Updater(config.jenialearn001bot_key, request_kwargs=PROXY)

        dp = mybot.dispatcher
        dp.add_handler(CommandHandler("start", greet_user))
        dp.add_handler(CommandHandler("wordcount", word_count))
        dp.add_handler(CommandHandler("wc", word_count))

        mybot.start_polling()
        mybot.idle()
    
# Вызываем функцию - эта строчка собственно запускает бота
main()

# try:
#     print('\n - - - Бот запущен - - - ')
#     main()
# except KeyboardInterrupt:
#         print('\n - - - Бот выключен - - - ')
