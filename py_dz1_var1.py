!#/usr/bin/python3
import re
import time
import datetime
# часть импорта для цветного вывода через colorama
import ctypes
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
#
from termcolor import colored, cprint
import colorama
from colorama import Fore, Back, Style
colorama.init()
#----

start = datetime.datetime.now().time() # время
date = datetime.date.today().year # год
print(start)
print(date)

error_counter = 0
print('\nКакая версия языка PYTHON сейчас актуальна?')
question1 = 'Python3'
while True:
    answer1 = str(input())
    answer1 = re.sub('[^A-Za-z0-9%А-Яа-я]','', answer1)
    if question1.lower() == answer1.lower():
        print(f'Ответ {answer1} верный')
        break
    elif str.lower(question1) != answer1:
        #print(f'Ответ НЕверный. \nПопробуй ещё раз.')
        print("\033[4m\033[37m\033[41m{}\033[0m".format("Неверный ответ. Попробуйте еще раз." + "\n"))
        error_counter+=1

print('\nКакая кодировка используется в строках?')
question2 = 'utf8'
while True:
    answer2 = str(input())
    answer2 = re.sub('[^A-Za-z0-9%А-Яа-я]','', answer2)
    if str.lower(question2) == str.lower(answer2):
        print(f'Ответ {answer1} верный')
        break
#        exit()
    elif str.lower(question2) != answer2:
#        print(f'Неверный ответ. Попробуйте еще раз.')
        print(Fore.RED + 'Неверный ответ. Попробуйте еще раз. \n')
        print(Style.RESET_ALL + 'ещё раз подумай: ')
        error_counter+=1

print('\nКак называется метод сортировки?')
question3 = 'sort'
while True:
    answer3 = str(input())
    answer3 = re.sub('[^A-Za-z0-9%А-Яа-я]','', answer3)
    if str.lower(question3) == str.lower(answer3):
        print(f'Ответ {answer3} верный')
        break
#        exit()
    elif str.lower(question3) != answer3:
        print('Ответ НЕверный. \nПопробуй ещё раз:')
        error_counter+=1

print('\nСколько значений есть у bool')
question4 = "2"
while True:
    answer4 = str(input())
    answer4 = re.sub('[^A-Za-z0-9%А-Яа-я]','', answer4)
    if question4 == answer4:
        print(f'Ответ {answer4} верный')
        break
#        exit()
    elif str.lower(question4) != answer4:
        print('Ответ НЕверный. \nПопробуй ещё раз:')
        error_counter+=1


print("\033[1;32;40m Поздравляем, вы ответили на n вопросов!  \n")
print(f"Кол-во ошибок за время теста: {error_counter} шт.")

# функция  re.sub() : для ввода любых символов в любом регистре;
# Использование re.sub для очистки ввода — это отличный подход, который делает проверку ответов более гибкой.

# функция str.lower : чтобы переменные question и answer совпадали с учётом re.sub() ;
# Приведение ответов к нижнему регистру с помощью str.lower() удобно для пользователя, так как игнорирует регистр.

# datetime.datetime.now().time() возвращает текущее время в Python. При этом дата будет игнорироваться;
# Вывод текущего времени и года может быть полезен для логирования.

## чтобы задать рекурсию вопроса в случае неправильного ответа, внутри цикла while нужно дать ответ,
## т.е. поставить break или exit() после совпадения значения строк в зависмости от завершения цикла/программы.
