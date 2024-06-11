import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from fractales.base import BaseFractale


class ComplexFractale(BaseFractale):
    """
    Use this class to create your own fractals
    
    Parameters
    ----------
    title : str
        The title of the fractal
    compute_z : function
        The function that computes z :
            - It takes z and c as parameters
            - It returns z
    max_iter : int
        The maximum number of iterations
    width : int
        The width of the image
    height : int
        The height of the image
    x_min : float
        The minimum value of the x axis
    x_max : float
        The maximum value of the x axis
    y_min : float
        The minimum value of the y axis
    y_max : float
        The maximum value of the y axis

    Publics methods
    ---------------
    - multibrot(cls, exponent: int = 2, max_iter: int = 20, *args, **kwargs) : Return the Multibrot Set
    - julia(cls, constant: complex, max_iter: int = 20, *args, **kwargs) : Return the Julia Set
    - burning_ship(cls, exponent: int = 2, max_iter: int = 20, *args, **kwargs) : Return the Burning Ship
    """
    def __init__(self, title: str, compute_z, max_iter: int, width: int = 800, height: int = 800, 
                 x_min: float = -1, x_max: float = 1, y_min: float = -1, y_max: float = 1):
        self._compute_z = compute_z
        self.max_iter = max_iter
        self.width = width
        self.height = height
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.x = np.linspace(self.x_min, self.x_max, self.width)
        self.y = np.linspace(self.y_min, self.y_max, self.height)
        super().__init__(title)

    def _generate_points(self) -> np.ndarray:
        z = np.zeros((self.height, self.width), dtype=np.complex128)
        c = self.x[np.newaxis, :] + 1j * self.y[:, np.newaxis]
        return self._iterate(z, c)
    
    def _iterate(self, z: np.ndarray, c: np.ndarray) -> np.ndarray:
        M = np.zeros(z.shape, dtype=int)
        mask = np.ones(z.shape, dtype=bool)
        for i in range(self.max_iter):
            z_new = np.zeros_like(z)
            z_new[mask] = self._compute_z(z[mask], c[mask])
            z[mask] = z_new[mask]
            mask[np.abs(z) >= 2] = False
            M[mask] = i
        return M
    
    def _specific_matplotlib_plot(self, ax: plt.Axes):
        ax.imshow(self.points)

    def _specific_plotly_plot(self, fig: go.Figure):
        fig.add_trace(go.Contour(z=self.points))

    # Factories
    @classmethod
    def multibrot(cls, exponent: int = 2, max_iter: int = 20, *args, **kwargs):
        """
        Create the Multibrot Set

        Parameters
        ----------
        exponent : int
            The exponent of the Mandelbrot Set
        max_iter : int
            The maximum number of iterations

        Returns
        ---------
        instance of ComplexFractale
            The Multibrot Set
        """
        def compute_z(z, c):
            return z ** exponent + c
        return cls(title="Mandelbrot Set", compute_z=compute_z, max_iter=max_iter, *args, **kwargs)

    @classmethod
    def julia(cls, constant: complex, max_iter: int = 20, *args, **kwargs):
        """
        Create the Julia Set

        Parameters
        ----------
        constant : complex
            The constant of the Julia Set
        max_iter : int
            The maximum number of iterations

        Returns
        ---------
        instance of ComplexFractale
            The Julia Set
        """
        def compute_z(z, c):

            new_z = z ** 2 + constant
            return new_z
        return cls(title="Julia Set", compute_z=compute_z, max_iter=max_iter, *args, **kwargs)

    @classmethod
    def burning_ship(cls, exponent: int = 2, max_iter: int = 20, *args, **kwargs):
        """
        Parameters
        ----------
        exponent : int
            The exponent of the Burning Ship
        max_iter : int
            The maximum number of iterations

        Returns
        ---------
        instance of ComplexFractale
            The Burning Ship
        """
        def compute_z(z: np.ndarray, c: np.ndarray) -> np.ndarray:
            return (np.abs(z.real) + 1j * np.abs(z.imag)) ** exponent + c

        return cls(title="Burning Ship", compute_z=compute_z, max_iter=max_iter, *args, **kwargs)
