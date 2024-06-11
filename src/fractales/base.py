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

    def plot_matplotlib(self, ax: plt.Axes | None = None, title: bool = True) -> plt.Figure:
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
    
    def _specific_plotly_plot(self, fig: go.Figure):
        raise NotImplementedError("Subclasses must implement this method")

    def plot_plotly(self, fig: go.Figure | None = None, title: bool = True) -> go.Figure:
        if fig is None:
            fig = go.Figure()
        else:
            fig = fig
        self._specific_plotly_plot(fig)
        
        fig.update_layout(width=800, height=800)
        if title:
            fig.update_layout(title=f"{self.title} ({self.order})")
        return fig
