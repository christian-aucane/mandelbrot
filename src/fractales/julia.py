import numpy as np
import matplotlib.pyplot as plt


class Julia:
    def __init__(self, width, height, max_iter):

        self.width, self.height = width, height  # Taille de l'image
        self.max_iter = max_iter  # Nombre maximum d'itérations
        self.c = complex(-0.4, 0.6)  # Constante de Julia


    # Appliquer l'itération de Julia
    def iteration_julia(self):
        # Créer une grille de points complexes
        x = np.linspace(-2, 2, self.width)
        y = np.linspace(-2, 2, self.height)
        X, Y = np.meshgrid(x, y)
        Z = X + 1j * Y
        # Initialiser l'image
        self.image = np.zeros(Z.shape, dtype=int)
        for _ in range(self.max_iter):
            mask = np.abs(Z) <= 2
            Z[mask] = Z[mask] ** 2 + self.c
            self.image[mask] += 1

    # Afficher l'image
    def show_img(self):
        plt.imshow(self.image, cmap='hot', extent=(-2, 2, -2, 2))
        plt.colorbar()
        plt.title('Ensemble de Julia')
        plt.show()

if __name__ == "__main__":
    x = Julia(800, 800, 255)
    x.iteration_julia()
    x.show_img()
