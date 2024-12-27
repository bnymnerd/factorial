import unittest
from main import factorial

class TestFactorial(unittest.TestCase):

    def test_factorial_zero(self):
        # 0! = 1 testini yapalım
        self.assertEqual(factorial(0), 1)

    def test_factorial_positive_number(self):
        # 5! = 120 testini yapalım
        self.assertEqual(factorial(5), 120)

    def test_factorial_large_number(self):
        # 10! = 3628800 testini yapalım
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_negative_number(self):
        # Negatif sayılar için hata fırlatılmalı
        with self.assertRaises(ValueError):
            factorial(-1)

if __name__ == "__main__":
    unittest.main()
