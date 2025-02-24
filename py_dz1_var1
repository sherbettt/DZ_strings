import re
import time
import datetime
# функция  re.sub() : для ввода любых символов в любом регистре
# функция str.lower : чтобы переменные question и answer совпадали с учётом re.sub()
# datetime.datetime.now().time() возвращает текущее время в Python. При этом дата будет игнорироваться.
## чтобы задать рекурсию вопроса в случае неправильного ответа, внутри цикла while нужно дать ответ,
## т.е. поставить break или exit() после совпадения значения строк в зависмости от завершения цикла/программы.

start = datetime.datetime.now().time() # время
date = datetime.date.today().year # год
print(start)
print(date)

print('Какая версия языка PYTHON сейчас актуальна?')
question1 = 'Python3'
while True:
    answer1 = str(input())
    answer1 = re.sub('[^A-Za-z0-9%А-Яа-я]','', answer1)
    if str.lower(question1) == str.lower(answer1):
        print(f'Ответ {answer1} верный')
        break
    elif str.lower(question1) != answer1:
        print(f'Ответ {answer1} НЕверный')

print('Какая кодировка используется в строках?')
question2 = 'utf8'
while True:
    answer2 = str(input())
    answer2 = re.sub('[^A-Za-z0-9%А-Яа-я]','', answer2)
    if str.lower(question2) == str.lower(answer2):
        print(f'Ответ {answer1} верный')
        break
    elif str.lower(question2) != answer2:
        print(f'Ответ {answer2} НЕверный')

print('Как называется метод сортировки?')
question3 = 'sort'
while True:
    answer3 = str(input())
    answer3 = re.sub('[^A-Za-z0-9%А-Яа-я]','', answer3)
    if str.lower(question3) == str.lower(answer3):
        print(f'Ответ {answer3} верный')
        break
    elif str.lower(question3) != answer3:
        print(f'Ответ {answer3} НЕверный')

print('Сколько значений есть у bool')
question4 = "2"
while True:
    answer4 = str(input())
    answer4 = re.sub('[^A-Za-z0-9%А-Яа-я]','', answer4)
    if question4 == answer4:
        print(f'Ответ {answer4} верный')
        break
#        exit()
    elif str.lower(question4) != answer4:
        print(f'Ответ {answer4} НЕверный')

