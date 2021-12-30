import matplotlib.pyplot as plt
import numpy as np

def times_data():
    times_file= open("times.txt", "r")
    times_list = times_file.readlines()
    print(times_list)
    


def demo():
    x = np.array(["A", "B", "C", "D"])
    y = np.array([3, 8, 1, 10])

    plt.bar(x,y)
    plt.show()



times_data()
