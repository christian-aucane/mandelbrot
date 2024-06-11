import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from .base import BaseFractale

    
class SierpinskiTriangle(BaseFractale):

    def __init__(self, order: int):
        super().__init__(title=f"Serpinski Triangle", order=order)

    def _recursive_sierpinski(self, vertices: np.ndarray, depth: int) -> np.ndarray:
        if depth == 0:
            return vertices[np.newaxis, :]
        
        rolled_vertices = np.roll(vertices, -1, axis=0)  # Roll the vertices
        midpoints = (vertices + rolled_vertices) / 2  # Compute the midpoints

        # Split the triangle into three smaller triangles
        t1 = np.array([vertices[0], midpoints[0], midpoints[2]])
        t2 = np.array([vertices[1], midpoints[1], midpoints[0]])
        t3 = np.array([vertices[2], midpoints[2], midpoints[1]])

        # Recursively split the smaller triangles
        triangles = np.vstack([
            self._recursive_sierpinski(t1, depth - 1),
            self._recursive_sierpinski(t2, depth - 1),
            self._recursive_sierpinski(t3, depth - 1)
        ])
        return triangles

    def _generate_points(self) -> np.ndarray:
        # Define the vertices of the triangle
        vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3) / 2]])

        triangles = self._recursive_sierpinski(vertices, self.order)
        return triangles

    def _specific_matplotlib_plot(self, ax: plt.Axes):
        for poly in self.points:
            # Add the polygon to the plot
            polygon = plt.Polygon(poly, edgecolor='black', fill=True)
            ax.add_patch(polygon)

    def _specific_plotly_plot(self, fig: go.Figure):
        for poly in self.points:
            # Ajouter le polygone au tracé
            fig.add_trace(go.Scatter(
                x=poly[:, 0],
                y=poly[:, 1],
                mode='lines',
                fill='toself',
                line=dict(color='black')
            ))

        # TODO : voir pourquoi il manque une ligne dans le tracé

        # Mise à jour du layout de la figure
        fig.update_layout(width=800, height=800)
        

if __name__ == "__main__":
    serpinski_triangle = SierpinskiTriangle(5)
    serpinski_triangle.plot_matplotlib()
    plt.show()
