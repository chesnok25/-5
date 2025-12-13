import pytest
import math
from src.calculator import Calculator

class TestCalculator:
    @pytest.fixture
    def calc(self):
        return Calculator()
    
    def test_add(self, calc):
        assert calc.add(2, 3) == 5
        assert calc.add(-1, 1) == 0
        assert calc.add(0, 0) == 0
        assert calc.add(2.5, 3.5) == 6.0
    
    def test_subtract(self, calc):
        assert calc.subtract(5, 3) == 2
        assert calc.subtract(3, 5) == -2
        assert calc.subtract(0, 0) == 0
    
    def test_multiply(self, calc):
        assert calc.multiply(2, 3) == 6
        assert calc.multiply(-2, 3) == -6
        assert calc.multiply(0, 5) == 0
        assert calc.multiply(2.5, 4) == 10.0
    
    def test_divide(self, calc):
        assert calc.divide(6, 3) == 2.0
        assert calc.divide(5, 2) == 2.5
        assert calc.divide(0, 5) == 0.0
    
    def test_divide_by_zero(self, calc):
        with pytest.raises(ValueError, match="Деление на ноль запрещено"):
            calc.divide(5, 0)
    
    def test_power(self, calc):
        assert calc.power(2, 3) == 8
        assert calc.power(5, 0) == 1
        assert calc.power(4, 0.5) == 2.0
        assert calc.power(2, -1) == 0.5
    
    def test_factorial(self, calc):
        assert calc.factorial(0) == 1
        assert calc.factorial(1) == 1
        assert calc.factorial(5) == 120
        assert calc.factorial(7) == 5040
    
    def test_factorial_negative(self, calc):
        with pytest.raises(ValueError, match="Факториал отрицательного числа не определен"):
            calc.factorial(-5)