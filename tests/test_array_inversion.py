import unittest

from array_inversion import inversion


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.first_list = [1, 2, 4, 7, 3]
        self.expected_first_list = [3, 7, 4, 2, 1]
        self.second_list = [10, 0, 0, 0, 0]
        self.expected_second_list = [0, 0, 0, 0, 10]

    def test_correct_return_firs_list(self):

        result = inversion(self.first_list, len(self.first_list))
        self.assertEqual(self.expected_first_list, result)

    def test_correct_return_second_list(self):

        result = inversion(self.second_list, len(self.second_list))
        self.assertEqual(self.expected_second_list, result)

    def test_incorrect_return_list(self):
        result = inversion([1, 2, 3, 4], 4)

        with self.assertRaises(AssertionError):
            self.assertEqual([3, 4, 2, 1], result)


if __name__ == '__main__':
    unittest.main()
