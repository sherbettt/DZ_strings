import re

# Список вопросов и ответов
questions = [
    {"question": "Какая версия языка PYTHON сейчас актуальна?", "answer": "Python3"},
    {"question": "Какая кодировка используется в строках?", "answer": "UTF8"},
    {"question": "Сколько значений есть у bool?", "answer": "2"},
    
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

print("Тестирование завершено!")
