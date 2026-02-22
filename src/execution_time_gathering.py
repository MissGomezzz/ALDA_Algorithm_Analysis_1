import time
from src.sorting import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
)
from src.data_generator import get_random_list


def take_time_for_algorithm(samples_array, sorting_function):
    times = []

    for sample in samples_array:
        start = time.perf_counter()
        sorting_function(sample.copy())
        end = time.perf_counter()

        times.append(end - start)

    times.sort()
    return times[len(times) // 2]  # medium


def take_times(size, samples_by_size):
    samples = []

    for _ in range(samples_by_size):
        samples.append(get_random_list(size))

    return [
        take_time_for_algorithm(samples, bubble_sort),
        take_time_for_algorithm(samples, selection_sort),
        take_time_for_algorithm(samples, insertion_sort),
        take_time_for_algorithm(samples, merge_sort),
        take_time_for_algorithm(samples, quick_sort),
    ]

def take_execution_time(minimum_size, maximum_size, step, samples_by_size):
    table = []

    for size in range(minimum_size, maximum_size + 1, step):
        print(f"Processing size: {size}")
        row = [size]
        times = take_times(size, samples_by_size)
        table.append(row + times)

    return table