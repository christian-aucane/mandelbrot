import streamlit as st
import matplotlib.pyplot as plt

from fractales import KochSnowflake, SierpinskiTriangle


FRACTALES_CLASSES = {
    "Sierpinski Triangle": SierpinskiTriangle,
    "Koch Snowflake": KochSnowflake
}

st.set_page_config(
    page_title="Fractales",
    page_icon="🎨",
)

def plot_fractal(fractal_class, order):
    fractal = fractal_class(order=order)
    fig, ax = plt.subplots()
    fractal.plot(ax=ax, title=False)
    st.pyplot(fig)

def main():
    fractale_type = st.sidebar.selectbox(
        "Choose a fractale",
        ("Sierpinski Triangle", "Koch Snowflake")
    )
    order = st.sidebar.slider("Order", 0, 8, 0)
    plot_fractal(FRACTALES_CLASSES[fractale_type], order)


if __name__ == "__main__":
    main()