import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_execution_times(results_list):
    """
    results_list: lista de listas
    Cada sublista: [size, algo1, algo2, algo3]
    """

    columns = ["Size", "Bubble", "Selection", "Insertion", "Merge", "Quick"]

    df = pd.DataFrame(results_list, columns=columns)

    sns.set(style="whitegrid")

    plt.figure()
    for algo in columns[1:]: 
        plt.plot(df["Size"], df[algo], label=algo)

    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (units)")
    plt.title("Sorting Algorithms Execution Time")
    plt.legend()
    plt.show()