import numpy as np
import matplotlib.pyplot as plt


class BaseFractale:

    def __init__(self, order: int, title: str):
        self.order = order
        self.title = title
        
        self.points = self.generate_points()

    def generate_points(self) -> np.ndarray:
        raise NotImplementedError("Subclasses must implement this method")
    
    def plot(self, ax: plt.Axes) -> plt.Figure:
        raise NotImplementedError("Subclasses must implement this method")

class SierpinskiTriangle(BaseFractale):

    def __init__(self, order: int):
        super().__init__(order, "Serpinski Triangle")

    def recursive_serpinski(self, vertices: np.ndarray, depth: int) -> np.ndarray:
        if depth == 0:
            return vertices[np.newaxis, :]
        
        midpoints = (vertices + np.roll(vertices, -1, axis=0)) / 2
        t1 = np.array([vertices[0], midpoints[0], midpoints[2]])
        t2 = np.array([vertices[1], midpoints[1], midpoints[0]])
        t3 = np.array([vertices[2], midpoints[2], midpoints[1]])
        triangles = np.vstack([
            self.recursive_serpinski(t1, depth - 1),
            self.recursive_serpinski(t2, depth - 1),
            self.recursive_serpinski(t3, depth - 1)
        ])
        return triangles

    def generate_points(self) -> np.ndarray:
        vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3) / 2]])
        triangles = self.recursive_serpinski(vertices, self.order)
        return triangles

    def plot(self, ax: plt.Axes = None) -> plt.Figure:
        if ax is None:
            fig, ax = plt.subplots()
        else:
            fig = ax.figure
        for poly in self.points:
            polygon = plt.Polygon(poly, edgecolor='black', fill=True)
            ax.add_patch(polygon)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title(f"{self.title} (ordre {self.order})")
        return fig


if __name__ == "__main__":
    serpinski_triangle = SierpinskiTriangle(5)
    serpinski_triangle.plot()
    plt.show()
