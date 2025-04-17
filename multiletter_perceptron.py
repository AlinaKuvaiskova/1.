# Модуль Urok2 - Распознавание букв
import random

# Обучающая выборка (идеальные изображения 10 букв: А, Б, В, Г, Д, Е, Ж, З, И, К)
letter_A = list('010101111101101')
letter_B = list('111101111101111')
letter_V = list('110101110101110')
letter_G = list('111100100100100')
letter_D = list('011101101101111')
letter_E = list('111100110100111')
letter_J = list('101111111111101')
letter_Z = list('111001111001111')
letter_I = list('101101101101111')
letter_K = list('101110100110101')

# Список всех букв
letters = [letter_A, letter_B, letter_V, letter_G, letter_D, letter_E, letter_J, letter_Z, letter_I, letter_K]
letter_names = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']

tema = 0  # Индекс буквы, которую распознаем — "А"
n_sensor = 3 * 5  # Размерность входа (3x5)
weights = [0 for i in range(n_sensor)]  # Обнуление весов

def perceptron(Sensor):
    B = 7  # Порог
    s = 0
    for i in range(n_sensor):
        s += int(Sensor[i]) * weights[i]
    return s >= B

def decrease(numer):
    for i in range(n_sensor):
        if int(numer[i]) == 1:
            weights[i] -= 1

def increase(numer):
    for i in range(n_sensor):
        if int(numer[i]) == 1:
            weights[i] += 1

# Тренировка сети
n = 10000
for i in range(n):
    j = random.randint(0, 9)
    r = perceptron(letters[j])
    if j != tema:
        if r:
            decrease(letters[j])
    else:
        if not r:
            increase(letters[j])

# Проверка на обучающей выборке
for i in range(10):
    print(f"{letter_names[i]} это А? ", perceptron(letters[i]))

# Примеры искажений для теста
letter_A1 = list('010101111100101')
letter_A2 = list('010100111101101')
print("Узнал А в A1? ", perceptron(letter_A1))
print("Узнал А в A2? ", perceptron(letter_A2))
