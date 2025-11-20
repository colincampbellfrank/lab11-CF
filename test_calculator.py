#https://github.com/colincampbellfrank/lab11-CF
import unittest
import calculator
from calculator import *

class TestCalculator(unittest.TestCase):


    def test_multiply(self): # 3 assertions
        self.assertEqual(calculator.mul(1,1),1)
        self.assertEqual(calculator.mul(0, 19218931), 0)
        self.assertEqual(calculator.mul(-2, -8), 16)
        self.assertEqual(calculator.mul(-1, 8), -8)

    def test_divide(self): # 3 assertions
        self.assertEqual(calculator.div(1, 1), 1)
        self.assertEqual(calculator.div(0, 1), "ZeroDivisionError")
        self.assertEqual(calculator.div(-4, -16), 4)


    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            calculator.logarithm(0,10)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(calculator.hypotenuse(4, 3), 5)
        self.assertEqual(calculator.hypotenuse(-4, 3), 5)
        self.assertEqual(calculator.hypotenuse(-4, -3), 5)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            calculator.square_root(-4)
        self.assertEqual(calculator.square_root(100), 10)
        self.assertEqual(calculator.square_root(16), 4)
        self.assertEqual(calculator.square_root(1), 1)

# Do not touch this
if __name__ == "__main__":
    unittest.main()