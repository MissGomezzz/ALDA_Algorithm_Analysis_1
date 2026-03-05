#Note: tests generated with ChatGPT

import unittest
from src.sorting import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
)


class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        self.unsorted_list = [5, 2, 9, 1, 5, 6]
        self.sorted_list = sorted(self.unsorted_list)

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort(self.unsorted_list), self.sorted_list)

    def test_selection_sort(self):
        self.assertEqual(selection_sort(self.unsorted_list), self.sorted_list)

    def test_insertion_sort(self):
        self.assertEqual(insertion_sort(self.unsorted_list), self.sorted_list)

    def test_merge_sort(self):
        self.assertEqual(merge_sort(self.unsorted_list), self.sorted_list)

    def test_quick_sort(self):
        self.assertEqual(quick_sort(self.unsorted_list), self.sorted_list)


if __name__ == "__main__":
    unittest.main()