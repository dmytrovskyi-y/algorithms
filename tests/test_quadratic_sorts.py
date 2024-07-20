import unittest

from quadratic_sorts import insertion_sort, bubble_sort, choice_sort


class MyTestCase(unittest.TestCase):
    """
    Quadratic sort testing class
    """
    @classmethod
    def setUpClass(cls):
        cls.list_numbers_insert_sort = [5, 4, 0, 12, 6, 2]
        cls.list_numbers_choice_sort = [17, 2, 0, 8, 6, 9]
        cls.list_numbers_bubble_sort = [1, 7, 3, 11, 8, 4]
        cls.expect_result_list_insert_sort = [0, 2, 4, 5, 6, 12]
        cls.expect_result_list_choice_sort = [0, 2, 6, 8, 9, 17]
        cls.expect_result_list_bubble_sort = [1, 3, 4, 7, 8, 11]

    def test_insertion_sort(self):
        """
        Tests Insertion sort
        """
        insertion_sort(self.list_numbers_insert_sort)
        self.assertEqual(self.expect_result_list_insert_sort, self.list_numbers_insert_sort)

    def test_choice_sort(self):
        """
        Tests Choice sort
        """
        choice_sort(self.list_numbers_choice_sort)
        self.assertEqual(self.expect_result_list_choice_sort, self.list_numbers_choice_sort)

    def test_bubble_sort(self):
        """
        Tests Bubble sort
        """
        bubble_sort(self.list_numbers_bubble_sort)
        self.assertEqual(self.expect_result_list_bubble_sort, self.list_numbers_bubble_sort)


if __name__ == '__main__':
    unittest.main()
