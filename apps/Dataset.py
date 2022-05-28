import requests
import streamlit as st
import plotly.express as px
from PIL import Image
import pandas as pd
from streamlit_lottie import st_lottie
import matplotlib.pyplot as plt
import seaborn as sn

def app():
    # Reading and Loading DataFrame

    csv_file = "cars_engage_2022.csv"
    df = pd.read_csv(csv_file)

    # Data Pre-processing

    df1 = df.drop("Unnamed: 0",axis=1) # droping the "Unnamed:0" column

    # Finding missing values

    sum1 = df1.isnull().sum()
    total = sum1.sort_values(ascending=False)
    percentage = sum1 * 100 / df1.isnull().count().sort_values(ascending=False)
    percentage.head()
    missing_data = pd.concat([total,percentage], axis=1, keys=['Total', 'Percentage'], sort=False).sort_values('Total', ascending=False)
    missing_data

    

   

    '''def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code !=200:
            return None 
        return r.json()

    #animation

    #animations = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_vvvmgeei.json")


    # DataFrame representation'''

    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    with st.container():
        left_column, right_column, mid_column = st.columns(3)


    with left_column:
         st.write("\nAutomobile Dataset")
         st.write( width=400)
         
         
    with right_column:
        st.write("Missing values")
        st.write(width=500)

    with mid_column:
        st.write("Description")
        st.write(width=400)

    with st.container():
        left_column, right_column, mid_column = st.columns(3)


    with left_column:
         st.dataframe(df1, width=400)
         st.write("shape =",df1.shape)
         
         
    with right_column:
        st.dataframe(missing_data, width=500)

    with mid_column:
        st.dataframe(df1.describe(), width=400)

    

