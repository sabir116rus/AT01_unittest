# test.py

import unittest
from main import add, subtract, multiply, divide, modulo


# Класс для тестирования математических функций
class TestMath(unittest.TestCase):

    # Тест для функции сложения
    def test_add(self):
        # Проверяем правильность сложения 2 и 5 (ожидаем 7)
        self.assertEqual(add(2, 5), 7)
        # Проверяем, что сумма 3 и 7 не равна 9
        self.assertNotEqual(add(3, 7), 9)

    # Тест для функции вычитания
    def test_subtract(self):
        # Проверяем правильность вычитания 4 из 7 (ожидаем 3)
        self.assertEqual(subtract(7, 4), 3)
        # Проверяем, что разница 4 и 2 не равна 1
        self.assertNotEqual(subtract(4, 2), 1)

    # Тест для функции умножения
    def test_multiply(self):
        # Проверяем, что произведение 2 и 5 не равно 12
        self.assertNotEqual(multiply(2, 5), 12)
        # Проверяем правильность умножения 3 на 6 (ожидаем 18)
        self.assertEqual(multiply(3, 6), 18)

    # Тест для функции деления
    def test_divide(self):
        # Проверяем, что результат деления 4 на 2 не равен 3
        self.assertNotEqual(divide(4, 2), 3)
        # Проверяем правильность деления 20 на 5 (ожидаем 4)
        self.assertEqual(divide(20, 5), 4)

    # Тест для проверки выброса исключения при делении на 0
    def test_divide_by_zero(self):
        # Проверяем, что при делении на 0 вызывается ValueError
        self.assertRaises(ValueError, divide, 6, 0)

    # Тест для функции вычисления остатка от деления
    def test_modulo(self):
        # Проверяем правильность вычисления остатка 10 % 3 (ожидаем 1)
        self.assertEqual(modulo(10, 3), 1)
        # Проверяем правильность вычисления остатка 6 % 4 (ожидаем 2)
        self.assertEqual(modulo(6, 4), 2)
        # Проверяем правильность вычисления остатка 7 % 7 (ожидаем 0)
        self.assertEqual(modulo(7, 7), 0)

    # Тест для проверки выброса исключения при попытке найти остаток от деления на 0
    def test_modulo_by_zero(self):
        # Проверяем, что при делении на 0 вызывается ValueError
        self.assertRaises(ValueError, modulo, 6, 0)


# Если этот файл запускается напрямую, запускаются тесты
if __name__ == '__main__':
    unittest.main()
