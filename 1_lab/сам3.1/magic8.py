import random

# Define variables.
name = "Roma"
question = "Примут ли у меня задание?"
answer = ""
random_number = random.randint(1, 12)

# Test
# print(random_number)

# Random choice.
if random_number == 1:
    answer = "Да, безусловно."
elif random_number == 2:
    answer = "Это решительно так."
elif random_number == 3:
    answer = "Без сомнения."
elif random_number == 4:
    answer = "Ответ туманный, попробуйте еще раз."
elif random_number == 5:
    answer = "Спросите еще раз позже."
elif random_number == 6:
    answer = "Лучше не говорить вам сейчас."
elif random_number == 7:
    answer = "Мои источники говорят «нет»."
elif random_number == 8:
    answer = "Прогноз не очень хороший."
elif random_number == 9:
    answer = "Очень сомнительно."
elif random_number == 10:
    answer = "Вероятность высока."
elif random_number == 11:
    answer = "Шансы равны."
elif random_number == 12:
    answer = "Все указывает на да."
else:
    answer = "Ошибка"

# Answer the question.
if question == "":
    print("Вопрос не задан.")
else:
    if name == "":
        print(f'Question: {question}')
    else:
        print(f'{name} спрашивает: {question}')
    print(f'Магический шар отвечает: {answer}')
