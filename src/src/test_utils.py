import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from utils import *

class TestUtils(unittest.TestCase):
    """Тесты для утилит"""
    
    def test_is_prime(self):
        """Тестирование проверки простых чисел"""
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(25))
    
    def test_fibonacci(self):
        """Тестирование чисел Фибоначчи"""
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)
    
    def test_fibonacci_negative(self):
        """Тестирование отрицательного индекса Фибоначчи"""
        with self.assertRaises(ValueError) as context:
            fibonacci(-1)
        self.assertEqual(str(context.exception), "Индекс должен быть неотрицательным")
    
    def test_reverse_string(self):
        """Тестирование реверса строки"""
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("привет"), "тевирп")

if __name__ == '__main__':
    unittest.main()