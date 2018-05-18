# Написать функцию ask_user() 
# чтобы с помощью input() спрашивать пользователя “Как дела?”
# При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”

# Переписать функцию ask_user(), добавив обработку exception-ов
# Добавить перехват ctrl+C и прощание

# Переписать функцию ask_user(), добавив обработку exception-ов
# Добавить перехват ctrl+C и прощание

def get_answer(question):
    answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
    return answers.get(question.lower(), ':-)')


def ask_user():
    try:
        while True:
            user_text = input('Как дела?: ')
            if user_text != 'Пока':
                print(get_answer(user_text))
            else:
                break
    except KeyboardInterrupt:
        print('\n  Извини за вопрос. Пока.')


ask_user()
