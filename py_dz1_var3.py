!#/usr/bin/python3

import re
import ctypes
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
import colorama
from colorama import Fore, Back, Style
colorama.init()


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
    {"question": "Как называется дробный тип данных?", "answer": "float"},
    {"question": "Достаточно вопросов? [Y]", "answer": "Y"},
]


def ask_question(question, correct_answer):
    error_counter = 0
    while True:
        user_answer = input(question + "\n").strip()
        user_answer = re.sub('[^A-Za-z0-9%А-Яа-я]', '', user_answer)  # Очистка ввода
        if user_answer.lower() == correct_answer.lower():
            print(Fore.GREEN + f"Ответ {user_answer} верный" + Style.RESET_ALL + "\n")
            break
        else:
            print("\033[4m\033[37m\033[41m{}\033[0m".format(f"Неверный ответ. Попробуйте еще раз."))
            error_counter+=1
            print(f"Кол-во ошибок за время теста: {error_counter} шт.")
            

# Основной цикл программы
for q in questions:
    ask_question(q["question"], q["answer"])

print("\033[1;32;40m Поздравляем, вы ответили на 10 вопросов!  \n")



# print("\033[1;32;40m Bright Green  \n")
# Функция strip() по умолчанию убирает пробелы в начале и в конце строки
# Символ новой строки в Python — это \n. Он используется для обозначения конца одной строки и начала новой.
