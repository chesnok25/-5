class Calculator:
    """Простой калькулятор с базовыми операциями"""
    
    def add(self, a: float, b: float) -> float:
        """Сложение двух чисел"""
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """Вычитание"""
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """Умножение"""
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """Деление с проверкой на ноль"""
        if b == 0:
            raise ValueError("Деление на ноль запрещено")
        return a / b
    
    def power(self, base: float, exponent: float) -> float:
        """Возведение в степень"""
        return base ** exponent
    
    def factorial(self, n: int) -> int:
        """Факториал числа"""
        if n < 0:
            raise ValueError("Факториал отрицательного числа не определен")
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result