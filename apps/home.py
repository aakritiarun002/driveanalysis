import requests
import streamlit as st
import plotly.express as px
from PIL import Image
import pandas as pd
from streamlit_lottie import st_lottie
import matplotlib.pyplot as plt
import seaborn as sn




def app():
    img = Image.open("bg4.jpg")
    st.image(img)

    
    
    st.markdown("---")
    # header
    '''with st.container():
        st.subheader("This website shows interactive data analysis :bar_chart:")
        st.write("Let's dive into analysis with great visualizations")'''


    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code !=200:
            return None 
        return r.json()

    #animation

    animations = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_3rqwsqnj.json")

    # How the website works

    with st.container():
        left_column, right_column = st.columns(2)
    with left_column:
        new = '<p style="font-family:sans-serif; color:whiteF; font-size: 42px;">About</p>'
        st.markdown(new, unsafe_allow_html=True)
        st.write("It began when we realized animals could carry us from one place to another. As the centuries rolled by we used this mobility to expand our horizons while at the same time seeking even better ways to travel.We harnessed the power of steams and began to replace animals with steams. But it was not until the development of the internal combustion engine that added a deep insight into our ways to improve the meaning of transport.In 1886, two vehicles were unveiled only  months apart by German engineers- Karl Benz and Gottileb Daimler, the automobile was born.")


    with right_column:
        st.image(Image.open("home.png"))

    st.markdown("---")

    with st.container():
        left_column, right_column = st.columns(2)
    with left_column:
        st.image(Image.open("home3.jpg"))

    with right_column:
        new = '<p style="font-family:sans-serif; color:whiteF; font-size: 42px;">What do the website do?</p>'
        st.markdown(new, unsafe_allow_html=True)
        st.write("The website shows interactive visualization of automotive Industry according to the comfort of the customer. The website performs data visualization on the automotive industry, important feature analysis of the dataset, and price analysis. With the help of Price Analysis, The Automotive Industry can understand the need of the market and easily manipulate the making of the car to fulfill the need of market needs. ")
    st.markdown("---")
    with st.container():
        st.image(Image.open("home2.png"))