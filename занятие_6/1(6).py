#вариант 4
s = "основы программирования"
s_new = s.replace("а", "о")
count = s.count("а")
length = len(s)
length_new = len(s_new)

print(f"Исходная строка: {s}")
print(f"Измененная строка: {s_new}")
print(f"Количество замен: {count}")
print(f"Количество символов в исходной строке: {length}")
print(f"Количество символов в измененной строке: {length_new}")
