from turtle import color
from pyparsing import White
import requests
import streamlit as st
import plotly.express as px
from PIL import Image
import pandas as pd
from streamlit_lottie import st_lottie
import matplotlib.pyplot as plt
import streamlit.components.v1 as components 
import seaborn as sn
from multiapp import MultiApp
from apps import home, Dataset, Value_count, range_features, price, signin # import your app modules here
img = Image.open("logo.png")
st.set_page_config(page_title="Drive Analysis", page_icon = "img", layout= "wide")

new_title = '<p style="font-family:sans-serif; color:whiteF; font-size: 42px;">Drive Analysis</p>'
st.markdown(new_title, unsafe_allow_html=True)

#st.header("Drive Analysis")
app = MultiApp()

pd.set_option("display.max_columns", 50)



# Add all your application here
app.add_app("Home", home.app)
app.add_app("Dataset", Dataset.app)
app.add_app("Data Visualization", Value_count.app)
app.add_app("Important Features Analysis", range_features.app)
app.add_app("Price Analysis", price.app)
app.add_app("Enquiry Form", signin.app)
# The main app
app.run()

# Footer 


from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb


def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)




def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 68px; },
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="white",
        text_align="center",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(2)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )



    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


def footer():
    myargs = [
        "Made with ",
        " with ❤️ by ",
        link("https://twitter.com/ArunAakriti", "@AakritiArun",  ),
    ]
    layout(*myargs)


if __name__ == "__main__":
    footer()

