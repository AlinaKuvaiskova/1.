#вариант 3
import math

def hypotenuse(cathet1, cathet2, cathet3, cathet4):
    hypotenuse1 = math.sqrt(cathet1**2 + cathet2**2)
    hypotenuse2 = math.sqrt(cathet3**2 + cathet4**2)
    if hypotenuse1 > hypotenuse2:
        print("Гипотенуза первого треугольника больше гипотенузы второго треугольника")
    elif hypotenuse1 < hypotenuse2:
        print("Гипотенуза второго треугольника больше гипотенузы первого треугольника")
    else:
        print("Длины гипотенуз равны")

cathet1 = 3
cathet2 = 4
cathet3 = 5
cathet4 = 12
hypotenuse(cathet1, cathet2, cathet3, cathet4)
