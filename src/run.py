from src.execution_time_gathering import take_execution_time
from src.plot_results import plot_execution_times
from src.data_generator import (
    get_random_list,
    get_sorted_list,
    get_reverse_sorted_list,
    get_nearly_sorted_list,
)

if __name__ == "__main__":

    random_results = take_execution_time(100, 1000, 100, 5, get_random_list)
    plot_execution_times(random_results)

    sorted_results = take_execution_time(100, 1000, 100, 5, get_sorted_list)
    plot_execution_times(sorted_results)

    reverse_results = take_execution_time(100, 1000, 100, 5, get_reverse_sorted_list)
    plot_execution_times(reverse_results)

    nearly_results = take_execution_time(100, 1000, 100, 5, get_nearly_sorted_list)
    plot_execution_times(nearly_results)