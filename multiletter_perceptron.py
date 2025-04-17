
import random

# Алфавит, который будем распознавать
alphabet = {
    'А': list('010101111101101'),
    'Л': list('100100100100111'),
    'И': list('101101101101111'),
    'Н': list('101101111101101'),
    'Б': list('111100111100111'),
    'В': list('110101110101110'),
    'Г': list('111100100100100'),
    'Е': list('111100110100111'),
    'К': list('101110100110101'),
    'М': list('101111111101101'),
}

# Параметры сети
n_sensor = 15  # 3x5 изображение
labels = list(alphabet.keys())
inputs = list(alphabet.values())
weights = {label: [0] * n_sensor for label in labels}

# Функция: возвращает, какую букву "узнал" перцептрон
def recognize(sensor):
    scores = {}
    for label in labels:
        score = sum(int(sensor[i]) * weights[label][i] for i in range(n_sensor))
        scores[label] = score
    return max(scores, key=scores.get)

# Функция обучения одного примера
def train_step(input_vector, correct_label):
    guessed_label = recognize(input_vector)
    if guessed_label != correct_label:
        # Ошибка — корректируем веса
        for i in range(n_sensor):
            if int(input_vector[i]) == 1:
                weights[correct_label][i] += 1
                weights[guessed_label][i] -= 1

# Обучение
n = 10000
for _ in range(n):
    idx = random.randint(0, len(inputs) - 1)
    train_step(inputs[idx], labels[idx])

# Проверка
print("Проверка на обучающей выборке:")
for i in range(len(labels)):
    recognized = recognize(inputs[i])
    print(f"Ожидалось: {labels[i]} — Распознано: {recognized}")

# Тест: немного искажённая "А"
test_A = list('010101111101100')
print("\nТест: немного искажённая А")
print("Распознано как:", recognize(test_A))
