import numpy as np
import matplotlib.pyplot as plt


class BaseFractale:

    def __init__(self, order, title):
        self.order = order
        self.title = title
        
        self.points = self.generate_points()

    def generate_points(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def plot(self):
        # TODO : retourner la figure, pas afficher (pour l'intégrer dans des subplots)
        _, ax = plt.subplots()
        for poly in self.points:
            poly = plt.Polygon(poly, edgecolor='black', fill=True)
            ax.add_patch(poly)
        ax.set_aspect('equal')
        ax.axis('off')
        plt.title(f"{self.title} (ordre {self.order})")
        plt.show()


class SierpinskiTriangle(BaseFractale):

    def __init__(self, order):
        super().__init__(order, "Serpinski Triangle")

    def recursive_serpinski(self, vertices, depth):
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

    def generate_points(self):
        vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3) / 2]])
        triangles = self.recursive_serpinski(vertices, self.order)
        return triangles


if __name__ == "__main__":
    serpinski_triangle = SierpinskiTriangle(5)
    serpinski_triangle.plot()
