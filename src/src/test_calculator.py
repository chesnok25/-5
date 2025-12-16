import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from calculator import Calculator

class TestCalculator(unittest.TestCase):
    """Тесты для класса Calculator"""
    
    def setUp(self):
        """Настройка перед каждым тестом"""
        self.calc = Calculator()
    
    def test_add(self):
        """Тестирование сложения"""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
    
    def test_subtract(self):
        """Тестирование вычитания"""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
    
    def test_multiply(self):
        """Тестирование умножения"""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
    
    def test_divide(self):
        """Тестирование деления"""
        self.assertEqual(self.calc.divide(6, 3), 2.0)
        self.assertAlmostEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(0, 5), 0.0)
    
    def test_divide_by_zero(self):
        """Тестирование деления на ноль"""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(5, 0)
        self.assertEqual(str(context.exception), "Деление на ноль запрещено")
    
    def test_power(self):
        """Тестирование возведения в степень"""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(4, 0.5), 2.0)
        self.assertEqual(self.calc.power(2, -1), 0.5)
    
    def test_factorial(self):
        """Тестирование факториала"""
        self.assertEqual(self.calc.factorial(0), 1)
        self.assertEqual(self.calc.factorial(1), 1)
        self.assertEqual(self.calc.factorial(5), 120)
        self.assertEqual(self.calc.factorial(7), 5040)
    
    def test_factorial_negative(self):
        """Тестирование факториала отрицательного числа"""
        with self.assertRaises(ValueError) as context:
            self.calc.factorial(-5)
        self.assertEqual(str(context.exception), "Факториал отрицательного числа не определен")

if __name__ == '__main__':
    unittest.main()