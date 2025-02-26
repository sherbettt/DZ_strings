import re
import time
import datetime


start = datetime.datetime.now().time()
date = datetime.date.today().year
print ('Добро пожаловать на тест, простой в действии, но сложен в реализации. '
       'В тесте разрешены русские и английские слова и регистры')
time.sleep(3)
print('Начинаем...')

question = {
1:'Какая версия языка сейчас актуальна?',
2:'Какая кодировка используется в строках?',
3:'Сколько значений есть у bool?',
4:'Название метода сортировки?',
5:'неизменяемая последовательность данных?',
6:'Где искать достоверную информацию по языку Python3?',
7:'Какой сейчас год?',
8:'Название переменной НИЧТО на английском?',
9:'Как называется дробный тип данных?',
10:'Достаточно вопросов? [Y]'
}

answer = {
1:'python3',
2:'utf8',
3:'2',
4:'sort',
5:'tuple',
6:'документация',
7: str(date),
8:'none',
9:'float',
10:'Y'
}

count = 0
for key in question.items():
    print(key[1])
    b=key[0]
    while True:
        n = str(input())
        n = re.sub('[^A-Za-z0-9%А-Яа-я]','', n)
        if str.lower(n) == answer[b]:
            print(f'Ваш ответ {n}, верный')
            break
        elif str.lower(n) != answer[b]:
            print(f'Ваш ответ {n}, не верный')
            count+=1
            stop = datetime.datetime.now().time()
print (f'Вы ответили на {b} вопросы и за все время тестирования у вас было {count} не верных ответов.'
       f'Время начала теста:{start} и время завершения теста: {stop} ')
