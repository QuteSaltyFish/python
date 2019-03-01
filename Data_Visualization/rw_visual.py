import matplotlib.pyplot as plt

from random_walk import RandomWalk


while True:
    # Make a random walk and plot the points.
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(figsize=(10, 6))
    point_number = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values,
                c=point_number, cmap=plt.cm.Blues, edgecolor='none', s=1)

    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)
    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running.lower() == 'n':
        break
