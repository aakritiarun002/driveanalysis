from turtle import color
import requests
from sqlalchemy import values
import streamlit as st
import plotly.express as px
from PIL import Image
import pandas as pd
from streamlit_lottie import st_lottie
import matplotlib.pyplot as plt
import seaborn as sn
import functions
from multiapp import MultiApp
from apps import home, Dataset, Value_count # import your app modules here
import plotly.express as px


def app():
    st.write("Data Visualization")
    # Reading and Loading DataFrame

    csv_file = "cars_engage_2022.csv"
    df = pd.read_csv(csv_file)

    # Data Pre-processing

    df = df.drop("Unnamed: 0",axis=1) # droping the "Unnamed:0" column


    with st.container():
        st.write("Select column:")    
        target_column = st.selectbox("", df.columns)
        st.subheader("Histogram Representation")
        fig = px.histogram(df, x = target_column)
        c1, c2, c3 = st.columns([0.5, 2, 0.5])
        c2.plotly_chart(fig)

    
    functions.space()
    st.write('<p style="font-size:130%" ></p>', unsafe_allow_html=True)



    with st.container():
        all_vizuals = [ 
                   'Distribution of Numerical Columns', 'Count Plots of Categorical Columns', 
                   'Box Plots']
        functions.sidebar_space(3)         
        vizuals = st.sidebar.multiselect("Data Visualization Dropdown", all_vizuals)


        num_columns = df.select_dtypes(exclude = 'object').columns
        cat_columns = df.select_dtypes(include = 'object').columns

        if 'Distribution of Numerical Columns' in vizuals:

            if len(num_columns) == 0:
                st.write('There is no numerical columns in the data.')
            else:
                selected_num_cols = functions.sidebar_multiselect_container('Choose columns for Distribution plots:', num_columns, 'Distribution')
                st.subheader('Distribution of numerical columns')
                i = 0
                while (i < len(selected_num_cols)):
                    c1, c2 = st.columns(2)
                    for j in [c1, c2]:

                        if (i >= len(selected_num_cols)):
                            break

                        fig = px.histogram(df, x = selected_num_cols[i])
                        j.plotly_chart(fig, use_container_width = True)
                        i += 1

        if 'Count Plots of Categorical Columns' in vizuals:

            if len(cat_columns) == 0:
                st.write('There is no categorical columns in the data.')
            else:
                selected_cat_cols = functions.sidebar_multiselect_container('Choose columns for Count plots:', cat_columns, 'Count')
                st.subheader('Count plots of categorical columns')
                i = 0
                while (i < len(selected_cat_cols)):
                    c1, c2 = st.columns(2)
                    for j in [c1, c2]:

                        if (i >= len(selected_cat_cols)):
                            break

                        fig = px.histogram(df, x = selected_cat_cols[i], color_discrete_sequence=['indianred'])
                        j.plotly_chart(fig)
                        i += 1

        if 'Box Plots' in vizuals:
            if len(num_columns) == 0:
                st.write('There is no numerical columns in the data.')
            else:
                selected_num_cols = functions.sidebar_multiselect_container('Choose columns for Box plots:', num_columns, 'Box')
                st.subheader('Box plots')
                i = 0
                while (i < len(selected_num_cols)):
                    c1, c2 = st.columns(2)
                    for j in [c1, c2]:
                    
                        if (i >= len(selected_num_cols)):
                            break
                    
                        fig = px.box(df, y = selected_num_cols[i])
                        j.plotly_chart(fig, use_container_width = True)
                        i += 1

        

        