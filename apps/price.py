import requests
import streamlit as st
import plotly.express as px
from PIL import Image
import pandas as pd
from streamlit_lottie import st_lottie
import matplotlib.pyplot as plt
import seaborn as sn



def app():
    st.title("Price Analysis")
    st.write("With the help of Price Analysis, The Automotive Industry can understand the need of the market and easily manipulate the making of the car to fulfill the need of market needs. ")

    # Reading and Loading DataFrame

    csv_file = "cars_engage_2022.csv"
    df = pd.read_csv(csv_file)

    # Data Pre-processing
    st.markdown("---")
    df = df.drop("Unnamed: 0",axis=1) # droping the "Unnamed:0" column
    df["Ex-Showroom_Price"] = df["Ex-Showroom_Price"].str.replace("Rs.", "").astype(str)
    df["Ex-Showroom_Price"] = df["Ex-Showroom_Price"].str.replace(",", "").astype(int)

    with st.container():
        st.write("Car Type vs Avg Price")
        df3=[~df["Body_Type"].isna()]
        df2 = df[~df["Type"].isna()]
        df2 = pd.DataFrame(df2.groupby(['Type'])['Ex-Showroom_Price'].mean().sort_values(ascending = False))
        st.bar_chart(df2)
    st.markdown("---")
    with st.container():
        st.write("Body Type vs Avg Price")
        df3= pd.DataFrame(df.groupby(['Body_Type'])['Ex-Showroom_Price'].mean().sort_values(ascending = False))
        st.bar_chart(df3)

    st.markdown("---")
    with st.container():
        st.write("Company Name vs Avg Price")
        df1= pd.DataFrame(df.groupby(['Make'])['Ex-Showroom_Price'].mean().sort_values(ascending = False))
        st.bar_chart(df1)
    st.markdown("---")
    with st.container():
        st.write("Fuel Type vs Avg Price")
        df[~df["Fuel_Type"].isna()]
        df = pd.DataFrame(df.groupby(['Fuel_Type'])['Ex-Showroom_Price'].mean().sort_values(ascending = False))
        st.bar_chart(df)
    st.markdown("---")


    

          


