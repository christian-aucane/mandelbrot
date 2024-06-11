
from base import BaseComplexFractale
import numpy as np
import matplotlib.pyplot as plt

class Multibrot(BaseComplexFractale):
    def __init__(self, order: int, exponent: int = 2):
        self.exponent = exponent
        super().__init__(title="Mandelbrot Set", order=order, x_min=-2.0, x_max=1.0, y_min=-1.5, y_max=1.5)

    def _compute_z(self, z: np.ndarray, c: np.ndarray) -> np.ndarray:
        return z**self.exponent + c
    

if __name__ == "__main__":
    mandelbrot = Multibrot(order=100, exponent=4)
    mandelbrot.plot()
    plt.show()