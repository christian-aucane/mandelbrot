import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go


class BaseFractale:

    def __init__(self, title: str, order: int = 3):
        self.order = order
        self.title = title
        self.points = self._generate_points()

    def _generate_points(self) -> np.ndarray:
        raise NotImplementedError("Subclasses must implement this method")
    
    def _specific_matplotlib_plot(self, ax: plt.Axes):
        raise NotImplementedError("Subclasses must implement this method")

    def _specific_plotly_plot(self, fig: go.Figure):
        raise NotImplementedError("Subclasses must implement this method")

    def plot_matplotlib(self, ax: plt.Axes | None = None, title: bool = True, library: str = "matplotlib") -> plt.Figure:    
        if ax is None:
            fig, ax = plt.subplots()
        else:
            fig = ax.figure

        self._specific_matplotlib_plot(ax)
        
        ax.set_aspect('equal')
        ax.axis('off')
        if title:
            ax.set_title(f"{self.title} ({self.order})")
        return fig
    
    def plot_plotly(self, title: bool = True):
        fig = go.Figure()
        self._specific_plotly_plot(fig)
        fig.update_layout(
            xaxis_visible=False,
            yaxis_visible=False,
            showlegend=False
            # width=self.width,
            # height=self.height
            
        )
        if title:
            fig.update_layout(title_text=f"{self.title} ({self.order})")
        return fig

class BaseComplexFractale(BaseFractale):
    def __init__(self, title: str, max_iter: int = 100, width: int = 800, height: int = 800, 
                 x_min: float = -1, x_max: float = 1, y_min: float = -1, y_max: float = 1):
        self.width = width
        self.height = height
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.x = np.linspace(self.x_min, self.x_max, self.width)
        self.y = np.linspace(self.y_min, self.y_max, self.height)
        self.max_iter = max_iter
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
            mask[np.abs(z) > 2] = False
            M[mask] = i
        
        return M

    def _compute_z(self, z: np.ndarray, c: np.ndarray) -> np.ndarray:
        raise NotImplementedError("Subclasses must implement this method")
    
    def _specific_matplotlib_plot(self, ax: plt.Axes):
        ax.imshow(self.points)

    def _specific_plotly_plot(self, fig: go.Figure):
        fig.add_trace(go.Heatmap(z=self.points))