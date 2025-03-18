
import numpy as np
import matplotlib.pyplot as plt

def plot_cell_one():
    # Create a new figure with specified dimensions (6 inches by 6 inches)
    plt.figure(figsize=(6, 6))
    # Create a scatter plot with the generated points in blue
    plt.scatter(x, y, color='blue')
    # Set the limits of the x-axis from 0 to 10
    plt.xlim(0, 10)
    # Set the limits of the y-axis from 0 to 10
    plt.ylim(0, 10)
    # Label the x-axis
    plt.xlabel('X-Axis')
    # Label the y-axis
    plt.ylabel('Y-Axis')
    # Set the title of the plot
    plt.title('Randomly Distributed Points in the Coordinate System')
    # Add a grid to the plot to improve readability
    plt.grid(True)
    # Display the plot
    plt.show()