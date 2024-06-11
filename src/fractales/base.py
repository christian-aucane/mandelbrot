import numpy as np
import matplotlib.pyplot as plt


class BaseFractale:

    def __init__(self, title: str, order: int = 3):
        self.order = order
        self.title = title
        self.points = self._generate_points()

    def _generate_points(self) -> np.ndarray:
        raise NotImplementedError("Subclasses must implement this method")
    
    def _specific_plot(self, ax: plt.Axes):
        raise NotImplementedError("Subclasses must implement this method")

    def plot(self, ax: plt.Axes | None = None, title: bool = True) -> plt.Figure:
        if ax is None:
            fig, ax = plt.subplots()
        else:
            fig = ax.figure

        self._specific_plot(ax)
        
        ax.set_aspect('equal')
        ax.axis('off')
        if title:
            ax.set_title(f"{self.title} ({self.order})")
        return fig
    