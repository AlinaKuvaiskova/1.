# Модуль Urok2 
import random 
# Обучающая выборка (идеальное изображение цифр от 0 до 9) 
num0 = list('111101101101111') 
num1 = list('001001001001001') 
num2 = list('111001111100111') 
num3 = list('111001111001111') 
num4 = list('101101111001001') 
num5 = list('111100111001111') 
num6 = list('111100111101111') 
num7 = list('111001001001001') 
num8 = list('111101111101111') 
num9 = list('111101111001111') 

# Список всех цифр от 0 до 9 в едином массиве 
nums = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9] 

tema = 5  # Какой цифре обучаем 
n_sensor = 3 * 5  # Количество сенсоров 
weights = [0 for i in range(n_sensor)]  # Обнуление весов 

# Функция определяет, является ли полученное изображение числом 5 
# Возвращает Да, если признано, что это 5. Возвращает Нет, если отвергнуто, что это 5 
def perceptron(Sensor): 
    B = 7  # Порог функции активации 
    s = 0  # Начальное значение суммы 
    for i in range(n_sensor):  # Цикл суммирования сигналов от сенсоров 
        s += int(Sensor[i]) * weights[i] 
    if s >= B: 
        return True  # Сумма превысила порог 
    else: 
        return False  # Сумма меньше порога 

# Уменьшение значений весов 
# Если сеть ошиблась и выдала Да при входной цифре, отличной от пятерки 
def decrease(numer): 
    for i in range(n_sensor): 
        if int(numer[i]) == 1:  # Возбужденный ли вход 
            weights[i] -= 1  # Уменьшаем связанный с входом вес на единицу 

# Увеличение значений весов 
# Если сеть не ошиблась и выдала Да при поданной на вход цифре 5 
def increase(numer): 
    for i in range(n_sensor): 
        if int(numer[i]) == 1:  # Возбужденный ли вход 
            weights[i] += 1  # Увеличиваем связанный с входом вес на единицу 

# Тренировка сети 
n = 10000  # Количество уроков 
for i in range(n): 
    j = random.randint(0, 9)  # Генерируем случайное число j от 0 до 9 
    r = perceptron(nums[j])  # Результат обращения к сумматору (ответ - Да или Нет) 
    if j != tema:  # Если генератор выдал случайное число j, не равное 5 
        if r:  # Если сумматор сказал Да (это пятерка), а j — это не пятерка. Ошибка. 
            decrease(nums[j])  # Наказываем сеть (уменьшаем значения весов) 
    else:  # Если генератор выдал число 5 
        if not r:  # Если сумматор сказал Нет — ошибка 
            increase(nums[j])  # Поощряем сеть (увеличиваем значения весов)
print(j) 
print("Веса") 
print(weights) # Вывод значений весов
print(weights) # Вывод значений весов 
# проверка работы программы на обучающей выборке 
print("0 это",tema,"? ", perceptron(nums[0])) 
print("1 это",tema,"? ", perceptron(nums[1])) 
print("2 это",tema,"? ", perceptron(nums[2])) 
print("3 это",tema,"? ", perceptron(nums[3])) 
print("4 это",tema,"? ", perceptron(nums[4])) 
print("5 это",tema,"? ", perceptron(nums[5])) 
print("6 это",tema,"? ", perceptron(nums[6])) 
print("7 это",tema,"? ", perceptron(nums[7])) 
print("8 это",tema,"? ", perceptron(nums[8])) 
print("9 это",tema,"? ", perceptron(nums[9])) 
num51 = list('111100111000111') 
num52 = list('111100010001111') 
num53 = list('111100011001111') 
num54 = list('110100111001111') 
num55 = list('110100111001011') 
num56 = list('111100101001111') 
# Прогон по тестовой выборке 
print("Узнал 5 в 51? ", perceptron(num51)) 
print("Yзнaл 5 в 52? ", perceptron(num52)) 
print("Узнал 5 в 53? ", perceptron(num53)) 
print("Узнал 5 в 54? ", perceptron(num54)) 
print("Yзнaл 5 в 55? ", perceptron(num55)) 
print("Узнал 5 в 56? ", perceptron(num56)) 
