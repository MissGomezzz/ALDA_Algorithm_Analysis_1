import random


def get_random_list(size, min_value=0, max_value=1_000_000):
    """
    Generates a list of random integers.

    Time Complexity: O(n)
    Space Complexity: O(n)

    :param size: Number of elements in the list
    :param min_value: Minimum possible value
    :param max_value: Maximum possible value
    :return: List of random integers
    """
    return [random.randint(min_value, max_value) for _ in range(size)]


def get_sorted_list(size):
    """
    Generates an already sorted list (ascending).

    Time Complexity: O(n)
    """
    return list(range(size))


def get_reverse_sorted_list(size):
    """
    Generates a reverse sorted list (descending).

    Time Complexity: O(n)
    """
    return list(range(size, 0, -1))


def get_nearly_sorted_list(size, swaps=10):
    """
    Generates a nearly sorted list by performing a few random swaps.

    Useful for analyzing best-case tendencies.

    Time Complexity: O(n)
    """
    arr = list(range(size))

    for _ in range(min(swaps, size)):
        i = random.randint(0, size - 1)
        j = random.randint(0, size - 1)
        arr[i], arr[j] = arr[j], arr[i]

    return arr