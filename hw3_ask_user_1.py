# Написать функцию ask_user() 
# чтобы с помощью input() спрашивать пользователя “Как дела?”,  пока он не ответит “Хорошо”

def ask_user():
    while True:
        user_text = input('Как дела?: ')
        if user_text == 'Хорошо':
            break


ask_user()
