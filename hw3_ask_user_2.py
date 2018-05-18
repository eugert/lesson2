# Написать функцию ask_user() 
# чтобы с помощью input() спрашивать пользователя “Как дела?”,  пока он не ответит “Хорошо”
# При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”

def get_answer(question):
    answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
    return answers.get(question.lower(), ':-)')


def ask_user():
    while True:
        user_text = input('Как дела?: ')
        if user_text != 'Пока':
            print(get_answer(user_text))
        else:
            break


ask_user()
