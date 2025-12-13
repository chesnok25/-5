import pytest
from src.utils import *

class TestUtils:
    def test_is_prime(self):
        assert is_prime(2) == True
        assert is_prime(3) == True
        assert is_prime(17) == True
        assert is_prime(1) == False
        assert is_prime(4) == False
        assert is_prime(9) == False
        assert is_prime(25) == False
    
    def test_fibonacci(self):
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1
        assert fibonacci(2) == 1
        assert fibonacci(3) == 2
        assert fibonacci(5) == 5
        assert fibonacci(10) == 55
    
    def test_fibonacci_negative(self):
        with pytest.raises(ValueError, match="Индекс должен быть неотрицательным"):
            fibonacci(-1)
    
    def test_reverse_string(self):
        assert reverse_string("hello") == "olleh"
        assert reverse_string("") == ""
        assert reverse_string("a") == "a"
        assert reverse_string("привет") == "тевирп"
    
    def test_count_vowels(self):
        assert count_vowels("hello") == 2
        assert count_vowels("HELLO") == 2
        assert count_vowels("xyz") == 0
        assert count_vowels("") == 0
        assert count_vowels("привет") == 2
        assert count_vowels("съешь ещё этих мягких французских булок") == 9