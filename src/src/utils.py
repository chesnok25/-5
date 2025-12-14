def is_prime(n: int) -> bool:
    """Проверка числа на простоту"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n: int) -> int:
    """Вычисление n-го числа Фибоначчи"""
    if n < 0:
        raise ValueError("Индекс должен быть неотрицательным")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def reverse_string(s: str) -> str:
    """Реверс строки"""
    return s[::-1]