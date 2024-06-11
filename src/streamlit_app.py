import streamlit as st

from fractales.koch_snowflake import KochSnowflake
from fractales.multibrot import Multibrot
from fractales.sierpinski import SierpinskiTriangle


class FractalesApp:
    # TODO : ajouter formules et petit texte dans les pages ?
    def __init__(self):
        self.pages = {
            "Sierpinski Triangle": self.sierpinski_triangle,
            "Koch Snowflake": self.kochnowflake,
            "Multibrot": self.multibrot,
            "Burning Ship": self.burning_ship
        }

    def sierpinski_triangle(self, librairy="matplotlib"):
        st.title("Sierpinski Triangle")

        st.sidebar.title("Parameters")
        order = st.sidebar.slider("Order", 0, 8, 0)

        self.plot_fractal(SierpinskiTriangle(order=order), librairy=librairy)

        # Ajouter références vers le code source

    def kochnowflake(self, librairy="matplotlib"):
        st.title("Koch Snowflake")
        st.sidebar.title("Parameters")
        order = st.sidebar.slider("Order", 0, 8, 0)

        self.plot_fractal(KochSnowflake(order=order), librairy=librairy)
        
        # Ajouter références vers le code source

    def multibrot(self, librairy="matplotlib"):
        st.title("Multibrot")
        st.sidebar.title("Parameters")

        max_iter = st.sidebar.slider("Max Iterations", 1, 1000, 100)
        exponent = st.sidebar.slider("Exponent", 1, 10, 2)
        multibrot_kwargs = {
            "width": st.sidebar.slider("Width", 100, 2000, 800),
            "height": st.sidebar.slider("Height", 100, 2000, 800),
            "x_min": st.sidebar.slider("x_min", -2, 2, -1),
            "x_max": st.sidebar.slider("x_max", -2, 2, 1),
            "y_min": st.sidebar.slider("y_min", -2, 2, -1),
            "y_max": st.sidebar.slider("y_max", -2, 2, 1)
        }

        multibrot = Multibrot(max_iter=max_iter, exponent=exponent, **multibrot_kwargs)

        self.plot_fractal(multibrot, librairy=librairy)
        # Ajouter références vers le code source

    def plot_fractal(self, fractal, librairy="matplotlib"):
        if librairy == "matplotlib":
            fig = fractal.plot_matplotlib(title=False)
            st.pyplot(fig)
        elif librairy == "plotly":
            fig = fractal.plot_plotly(title=False)
            st.plotly_chart(fig)
        # TODO : ajouer animation ici ?
        # TODO : utiliser plotly

    def run(self):
        st.sidebar.title("Navigation")
        selection = st.sidebar.radio("Go to", list(self.pages.keys()))
        page = self.pages[selection]
        # TODO : ajouter choix de la palete de couleurs
        library = st.sidebar.radio("Plotting library", ("matplotlib", "plotly"))
        page(librairy=library)


if __name__ == "__main__":
    app = FractalesApp()
    app.run()
