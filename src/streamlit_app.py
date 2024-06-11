import streamlit as st

from fractales.complex import ComplexFractale
from fractales.koch_snowflake import KochSnowflake
from fractales.sierpinski import SierpinskiTriangle


class FractalesApp:
    # TODO : ajouter formules et petit texte dans les pages ?
    def __init__(self):
        self.pages = {
            "Sierpinski Triangle": self.sierpinski_triangle,
            "Koch Snowflake": self.koch_snowflake,
            "Multibrot Set": self.multibrot_set,
            "Julia Set": self.julia_set,
            "Burning Ship": self.burning_ship
        }

    def sierpinski_triangle(self, librairy="matplotlib"):
        st.title("Sierpinski Triangle")

        st.sidebar.title("Parameters")
        order = st.sidebar.slider("Order", 0, 8, 0)

        self.plot_fractal(SierpinskiTriangle(order=order), librairy=librairy)

        # Ajouter références vers le code source

    def koch_snowflake(self, librairy="matplotlib"):
        st.title("Koch Snowflake")
        st.sidebar.title("Parameters")
        order = st.sidebar.slider("Order", 0, 8, 0)

        self.plot_fractal(KochSnowflake(order=order), librairy=librairy)
        
        # Ajouter références vers le code source

    def complex_factory_kwargs(self):
        return {
            "width": st.sidebar.slider("Width", 100, 2000, 800),
            "height": st.sidebar.slider("Height", 100, 2000, 800),
            "x_min": st.sidebar.slider("x_min", -2, 2, -1),
            "x_max": st.sidebar.slider("x_max", -2, 2, 1),
            "y_min": st.sidebar.slider("y_min", -2, 2, -1),
            "y_max": st.sidebar.slider("y_max", -2, 2, 1)
        }

    def multibrot_set(self, librairy="matplotlib"):
        st.title("Multibrot Set")
        st.sidebar.title("Parameters")

        max_iter = st.sidebar.slider("Max Iterations", 1, 1000, 100)
        exponent = st.sidebar.slider("Exponent", 1, 10, 2)
        multibrot_kwargs = self.complex_factory_kwargs()
        multibrot = ComplexFractale.multibrot(exponent=exponent, max_iter=max_iter, **multibrot_kwargs)

        self.plot_fractal(multibrot, librairy=librairy)
        # Ajouter références vers le code source

    def julia_set(self, librairy="matplotlib"):
        st.title("Julia Set")

        max_iter = st.sidebar.slider("Max Iterations", 1, 1000, 100)
        real_part = st.sidebar.slider("Real Part", -2.0, 2.0, 0.0)
        imaginary_part = st.sidebar.slider("Imaginary Part", -2.0, 2.0, 0.0)
        julia_kwargs = self.complex_factory_kwargs()
        constant = complex(real_part, imaginary_part)
        print("julia_constant", constant)

        julia = ComplexFractale.julia(constant=complex(real_part, imaginary_part), max_iter=max_iter, **julia_kwargs)
        self.plot_fractal(julia, librairy=librairy)

    def burning_ship(self, librairy="matplotlib"):
        st.title("Burning Ship")
        max_iter = st.sidebar.slider("Max Iterations", 1, 1000, 100)
        exponent = st.sidebar.slider("Exponent", 1, 10, 2)

        burning_ship_kwargs = self.complex_factory_kwargs()
        
        burning_ship = ComplexFractale.burning_ship(exponent=exponent, max_iter=max_iter, **burning_ship_kwargs)

        self.plot_fractal(burning_ship, librairy=librairy)

    def plot_fractal(self, fractal, librairy="matplotlib"):
        if librairy == "matplotlib":
            fig = fractal.plot_matplotlib(title=False)
            st.pyplot(fig)
        elif librairy == "plotly":
            fig = fractal.plot_plotly(title=False)
            st.plotly_chart(fig)

    def run(self):
        nav_option = st.sidebar.selectbox('Fractale', list(self.pages.keys()))

        # TODO : ajouter choix de la palete de couleurs ?
        library = st.sidebar.selectbox("Plotting library", ("matplotlib", "plotly"))
        
        page = self.pages[str(nav_option)]
        
        page(librairy=str(library))

if __name__ == "__main__":
    app = FractalesApp()
    app.run()
