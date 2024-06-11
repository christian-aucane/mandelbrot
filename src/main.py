import matplotlib.pyplot as plt

from fractales import SierpinskiTriangle
from fractales.koch_snowflake import KochSnowflake
from fractales.multibrot import Multibrot


def plot_all_fractales(fractale_classes, min_order=0, max_order=5):
    num_fractales = len(fractale_classes)
    fig = plt.figure(figsize=(15, 3 * num_fractales))
    
    for i, fractale_class in enumerate(fractale_classes):
        for order in range(min_order, max_order + 1):
            ax = fig.add_subplot(num_fractales, max_order + 1, i * (max_order + 1) + order + 1)
            fractale = fractale_class(order=order)
            fractale.plot(ax)
    plt.subplots_adjust(hspace=0.5)
    plt.show()


def main():
    fractale_classes = [
        SierpinskiTriangle,
        KochSnowflake,
        Multibrot
    ]
    # TODO : ajouter un argument pour le min_order et le max_order

    plot_all_fractales(fractale_classes)

if __name__ == "__main__":
    main()
    