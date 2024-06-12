import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

try:
    from .base import BaseFractale
except ImportError:
    from base import BaseFractale


class PythagorasTree(BaseFractale):
    def __init__(self, order: int, bottom: np.ndarray = np.array([[-50., 0], [50., 0]])):
        # TODO : ajouter argument pour déterminer la forme des triangle
        self.bottom = bottom
        super().__init__(title="Pythagoras Tree", order=order)

    def _generate_points(self) -> np.ndarray:
        # Définir les points de départ pour l'arbre
        squares = self.recursive_generate_square(bottom=self.bottom, depth=self.order)
        return squares

    def _compute_appex_point(self, segment: np.ndarray):
        # https://en.wikipedia.org/wiki/Pythagorean_tree
        # TODO : modifier pour ajouter le parametre
        X1, Y1 = segment[0]
        X2, Y2 = segment[1]
        A = (X1 + X2) / 2 - (Y2 - (Y2 + Y1) / 2)
        B = (Y1 + Y2) / 2 + (X2 - (X2 + X1) / 2)
        C = X1 - (B - Y1)
        D = Y1 + (A - X1)
        E = A - (B - Y1)
        F = B + (A - X1)
        G = A - (Y2 - B)
        H = B + (X2 - A)
        I = X2 - (Y2 - B)
        J = Y2 + (X2 - A)
        appex_point = np.array([A, B])
        
        return np.array([A, B])    

    def recursive_generate_square(self, bottom: np.ndarray, depth: int) -> np.ndarray:
        start, end = bottom

        vector = end - start
        square_width = np.linalg.norm(vector)
        
        outward_direction = np.array([-vector[1], vector[0]]) / np.linalg.norm(vector)  # Normalize perpendicular vector        top_right = end + outward_direction
        
        top_right = end + outward_direction * square_width
        top_left = start + outward_direction * square_width
        square = np.array([start, end, top_right, top_left])
          
        if depth == 0:
            return square[np.newaxis, :]
        appex_point = self._compute_appex_point(np.array([top_left, top_right]))
        
        s1_bottom = np.array([top_left, appex_point])
        s2_bottom = np.array([appex_point, top_right])

        squares = np.vstack([
            square[np.newaxis, :],
            self.recursive_generate_square(bottom=s1_bottom, depth=depth - 1),
            self.recursive_generate_square(bottom=s2_bottom, depth=depth - 1)
        ])

        return squares

    def _specific_matplotlib_plot(self, ax: plt.Axes):
        # Ajouter chaque segment au graphique
        for square in self.points:
            # Add the polygon to the plot
            polygon = plt.Polygon(square, edgecolor='black', fill=True)
            ax.add_patch(polygon)
        start, end = self.bottom
        square_width = int(np.linalg.norm(end - start).round(0))

        ax.set_xlim(-3 * square_width, 3 * square_width)
        ax.set_ylim(0, 4*square_width)

    def _specific_plotly_plot(self, fig: go.Figure):
        # TODO : corriger affichage plotly
        print("self.points.shape : ", self.points.shape)
        for square in self.points:
            np.vstack([square[0], square])
            x = square[:, 0]
            y = square[:, 1]
            # Add the polygon to the plot
            fig.add_trace(go.Scatter(
                x=x,
                y=y,
                mode='lines',
                line=dict(color='black')
            ))
        # Mise à jour du layout de la figure
        fig.update_layout(width=800, height=800)


if __name__ == "__main__":
    tree = PythagorasTree(5)
    tree.plot_matplotlib(axis=True)
    plt.show()
