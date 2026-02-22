from src.execution_time_gathering import take_execution_time
from src.plot_results import plot_execution_times

if __name__ == "__main__":
    results = take_execution_time(minimum_size=100, maximum_size=1000, step=100, samples_by_size=5)
    plot_execution_times(results)