# main.py

# Функция сложения двух чисел
def add(a, b):
    return a + b

# Функция вычитания второго числа из первого
def subtract(a, b):
    return a - b

# Функция умножения двух чисел
def multiply(a, b):
    return a * b

# Функция деления первого числа на второе
# Если второе число равно 0, выбрасывается ошибка ValueError
def divide(a, b):
    if b == 0:
        raise ValueError("На ноль делить нельзя")
    return a / b

# Функция для вычисления остатка от деления первого числа на второе
# Если второе число равно 0, выбрасывается ошибка ValueError
def modulo(a, b):
    if b == 0:
        raise ValueError("На ноль делить нельзя")
    return a % b
