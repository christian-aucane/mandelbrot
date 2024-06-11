from .base import BaseComplexFractale
import numpy as np
import matplotlib.pyplot as plt

class Multibrot(BaseComplexFractale):
    def __init__(self, max_iter: int, exponent: int = 2, *args, **kwargs):
        self.exponent = exponent
        self.max_iter = max_iter
        super().__init__(title="Multibrot Set", *args, **kwargs)

    def _compute_z(self, z: np.ndarray, c: np.ndarray) -> np.ndarray:
        return z**self.exponent + c
    

if __name__ == "__main__":
    mandelbrot = Multibrot(max_iter=100)
    mandelbrot.plot_matplotlib()
    plt.show()