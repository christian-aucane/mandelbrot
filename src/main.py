import argparse

import matplotlib.pyplot as plt

from fractales import SierpinskiTriangle

def sierpinski_triangle(max_order=5):
    fig, axs = plt.subplots(1, max_order + 1, figsize=(15, 5))
    for order in range(0, max_order + 1):
        sierpinski = SierpinskiTriangle(order=order)
        sierpinski.plot(axs[order])
    plt.tight_layout()
    plt.show()


def main():

    sierpinski_triangle(max_order=5)


if __name__ == "__main__":
    main()
    