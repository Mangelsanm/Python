import matplotlib.pyplot as plt
import random

def estimate_pi(n):
    point_circle = 0
    point_total = 0

    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            point_circle += 1
            plt.plot(x, y, 'bo')
        else:
            plt.plot(x, y, 'ro')
        point_total += 1
    plt.show()

    pi = 4 * point_circle / point_total
    print(pi)

estimate_pi(1000)