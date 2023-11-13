import unittest
from math_quiz import random_integer_generator, random_operator_selection, mathematical_operation


class TestMathGame(unittest.TestCase):

    def test_random_integer_generator(self):
        # Test if random numbers generated are within the specified range
        min_value = 1
        max_value = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer_generator(min_value, max_value)
            self.assertTrue(min_value <= rand_num <= max_value)

    def test_random_operator_selection(self):
        # Test if the generated random operator is '+', '-' or '*'
        possible_operators = {'+','-','*'}
        for _ in range(1000):  # Test a large number of random values
            rand_ope = random_operator_selection()
            self.assertIn(rand_ope, possible_operators)

    def test_mathematical_operation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (4, 6, '+', '4 + 6', 10),
                (1, 8, '+', '1 + 8', 9),
                (5, 2, '-', '5 - 2', 3),
                (4, 6, '-', '4 - 6', -2),
                (1, 8, '-', '1 - 8', -7),
                (5, 2, '*', '5 * 2', 10),
                (4, 6, '*', '4 * 6', 24),
                (1, 8, '*', '1 * 8', 8),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                operation, result = mathematical_operation(num1,num2,operator)
                self.assertEqual(operation, expected_problem)
                self.assertEqual(result,expected_answer)

if __name__ == "__main__":
    unittest.main()
