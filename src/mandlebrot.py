import numpy as np
import matplotlib.pyplot as plt

# Mandelbrot Set

def mandelbrot(c, max_iter=100):
    """
    Computes the number of iterations needed to determine if a complex number c belongs to the Mandelbrot set.
    Args:
        c (complex): The complex number to check.
        max_iter (int, optional): Maximum number of iterations. Defaults to 100.
    Returns:
        int: Number of iterations.
    """
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    """
    Generates the Mandelbrot set within a specified region.
    Args:
        xmin, xmax, ymin, ymax (float): Boundaries of the set.
        width, height (int): Dimensions of the grid.
        max_iter (int): Maximum number of iterations.
    Returns:
        tuple: (r1, r2, mandelbrot_array)
            r1, r2 (numpy arrays): Grid points in the complex plane.
            mandelbrot_array (numpy array): Mandelbrot set data.
    """
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1, r2, np.array([[mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2]))

def display(xmin, xmax, ymin, ymax, width, height, max_iter):
    """
    Displays the Mandelbrot set.
    Args:
        xmin, xmax, ymin, ymax (float): Boundaries of the set.
        width, height (int): Dimensions of the grid.
        max_iter (int): Maximum number of iterations.
    """
    d = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    plt.imshow(d[2], extent=(xmin, xmax, ymin, ymax))
    plt.show()

# Display the Mandelbrot set
display(-2.0, 0.5, -1.25, 1.25, 1000, 1000, 100)
