import numpy as np
import matplotlib.pyplot as plt

# mandlebrot

def mandelbrot(c, max_iter=100): # c is a complex number 
    z = 0 # z is a complex number
    n = 0 # n is the number of iterations
    while abs(z) <= 2 and n < max_iter: # abs is the absolute value
        z = z*z + c
        n += 1
    return n # return the number of iterations

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter): # xmin, xmax, ymin, ymax are the boundaries of the set
    r1 = np.linspace(xmin, xmax, width) # r1 is a numpy array of evenly spaced numbers over a specified interval
    r2 = np.linspace(ymin, ymax, height) # r2 is a numpy array of evenly spaced numbers over a specified interval
    return (r1, r2, np.array([[mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2])) # return the mandelbrot set

def display(xmin, xmax, ymin, ymax, width, height, max_iter): # display the mandelbrot set
    d = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter) # d is the mandelbrot set
    plt.imshow(d[2], extent=(xmin, xmax, ymin, ymax)) # display the mandelbrot set
    plt.show() 

display(-2.0, 0.5, -1.25, 1.25, 1000, 1000, 100) # display the mandelbrot set
