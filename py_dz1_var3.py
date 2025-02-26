import re
#import sys


# Список вопросов и ответов
questions = [
    {"question": "Какая версия языка PYTHON сейчас актуальна?", "answer": "Python3"},
    {"question": "Какая кодировка используется в строках?", "answer": "UTF8"},
    {"question": "Сколько значений есть у bool?", "answer": "2"},
    {"question": "Название метода сортировки?", "answer": "sort"},
    {"question": "неизменяемая последовательность данных?", "answer": "tuple"},
    {"question": "Каким оператором можно досрочно прервать цикл?", "answer": "break"},
    {"question": "Исключающее ИЛИ?", "answer": "XOR"},
    {"question": "Название переменной НИЧТО на английском?", "answer": "none"},
    {"question": "Какой сейчас год??", "answer": "2025"},
    {"question": "Достаточно вопросов? [Y]", "answer": "Y"},
]

def ask_question(question, correct_answer):
    while True:
        user_answer = input(question + "\n").strip()
        user_answer = re.sub('[^A-Za-z0-9%А-Яа-я]', '', user_answer)  # Очистка ввода
        if user_answer.lower() == correct_answer.lower():
            print(f"Ответ {user_answer} верный")
            break
        else:
            print("Неверный ответ. Попробуйте еще раз.")

# Основной цикл программы
for q in questions:
    ask_question(q["question"], q["answer"])

print("\033[1;32;40m Bright Green  \n")
print("Поздравляем, вы ответили на 10 вопросов!")


# print("\033[1;32;40m Bright Green  \n")
# Функция strip() по умолчанию убирает пробелы в начале и в конце строки
# Символ новой строки в Python — это \n. Он используется для обозначения конца одной строки и начала новой.
