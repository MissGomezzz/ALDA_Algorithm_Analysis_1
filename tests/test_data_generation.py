#Note: tests generated with ChatGPT


import unittest
from src.data_generator import (
    get_random_list,
    get_sorted_list,
    get_reverse_sorted_list,
    get_nearly_sorted_list,
)


class TestDataGenerator(unittest.TestCase):

    def test_random_list_size(self):
        arr = get_random_list(10)
        self.assertEqual(len(arr), 10)

    def test_sorted_list(self):
        arr = get_sorted_list(10)
        self.assertEqual(arr, list(range(10)))

    def test_reverse_sorted_list(self):
        arr = get_reverse_sorted_list(5)
        self.assertEqual(arr, [5, 4, 3, 2, 1])

    def test_nearly_sorted_size(self):
        arr = get_nearly_sorted_list(10)
        self.assertEqual(len(arr), 10)


if __name__ == "__main__":
    unittest.main()