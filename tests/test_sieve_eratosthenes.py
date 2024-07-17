"""Sieve of Eratosthenes algorithm testing module"""
import unittest
from sieve_eratosthenes import sieve_eratosthenes


class MyTestCase(unittest.TestCase):
    """
    Sieve of Eratosthenes algorithm testing class
    """
    @classmethod
    def setUpClass(cls):
        cls.length_limit = 19
        cls.expect_result = [2, 3, 5, 7, 11, 13, 17]

    def test_get_correct_result(self) -> None:
        """
        Test of obtaining the correct result from the operation of the algorithm
        """
        result = sieve_eratosthenes(length=self.length_limit)
        self.assertEqual(self.expect_result, result)


if __name__ == '__main__':
    unittest.main()
