import numpy as np
from .base import BaseFractale


class Multibrot(BaseFractale):
    def __init__(self, power=3, xmin=-2.0, xmax=0.5, ymin=-1.25, ymax=1.25, width=720, height=480, max_iter=None, title="Multibrot", order=3):
        self.power = power
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.width = width
        self.height = height
        self.max_iter = max_iter if max_iter is not None else self.iterations(order)
        super().__init__(title, order)

    def iterations(self, order):
        return [1, 5, 10, 20, 50, 100][order]

    def multibrot(self, c):
        z = 0
        n = 0
        while abs(z) <= 2 and n < self.max_iter:
            z = z**self.power + c
            n += 1
        return n

    def _generate_points(self):
        r1 = np.linspace(self.xmin, self.xmax, self.width)
        r2 = np.linspace(self.ymin, self.ymax, self.height)
        return (r1, r2, np.array([[self.multibrot(complex(r, i)) for r in r1] for i in r2]))

    def _specific_plot(self, ax):
        d = self._generate_points()
        ax.imshow(d[2], extent=(self.xmin, self.xmax, self.ymin, self.ymax))
