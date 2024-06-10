import numpy as np
import matplotlib.pyplot as plt


class BaseFractale:

    def __init__(self, order: int, title: str):
        self.order = order
        self.title = title
        self.points = self._generate_points()

    def _generate_points(self) -> np.ndarray:
        raise NotImplementedError("Subclasses must implement this method")
    
    def _specific_plot(self, ax: plt.Axes):
        raise NotImplementedError("Subclasses must implement this method")
    
    def plot(self, ax: plt.Axes | None=None) -> plt.Figure:
        if ax is None:
            fig, ax = plt.subplots()
        else:
            fig = ax.figure

        self._specific_plot(ax)
        
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title(f"{self.title} (ordre {self.order})")
        return fig
    
class SierpinskiTriangle(BaseFractale):

    def __init__(self, order: int):
        super().__init__(order, "Serpinski Triangle")

    def _recursive_sierpinski(self, vertices: np.ndarray, depth: int) -> np.ndarray:
        if depth == 0:
            return vertices[np.newaxis, :]
        
        # Compute the midpoints of the edges
        midpoints = (vertices + np.roll(vertices, -1, axis=0)) / 2

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

    def _specific_plot(self, ax: plt.Axes):
        for poly in self.points:
            # Add the polygon to the plot
            polygon = plt.Polygon(poly, edgecolor='black', fill=True)
            ax.add_patch(polygon)
        

if __name__ == "__main__":
    serpinski_triangle = SierpinskiTriangle(5)
    serpinski_triangle.plot()
    plt.show()
