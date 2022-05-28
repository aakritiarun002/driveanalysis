from cmath import nan
from stat import FILE_ATTRIBUTE_SPARSE_FILE
from matplotlib import container
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
from sympy import N
#from sklearn.linear_model import LogisticRegression
#from sklearn.naive_bayes import MultinomialNB
#from sklearn.ensemble import RandomForestClassifier
#from sklearn.model_selection import train_test_split


def app():
    #st.title('Data Visualization')

    # Reading csv file
    csv_file = "cars_engage_2022.csv"
    df = pd.read_csv(csv_file)
    df = df.drop("Unnamed: 0",axis=1) # droping the "Unnamed:0" column
    sum1 = df.isnull().sum()
    total = sum1.sort_values(ascending=False)
    percentage = sum1 * 100 / df.isnull().count().sort_values(ascending=False)
    percentage.head()
    missing_data = pd.concat([total,percentage], axis=1, keys=['Total', 'Percentage'], sort=False).sort_values('Total', ascending=False)
    missing_data
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    
    #st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#C9DEF5;" /> """, unsafe_allow_html=True)
    #cleaning data

    with st.container():
        left_column, mid_column, right_column = st.columns(3)

    with left_column:
        st.write("Make")
        st.write(df["Make"].unique()) # "<NA>" value present
    with right_column:
        st.write("Variant")
        st.write(df["Variant"].unique()) # no missing value present

    with mid_column:
        st.write("Price")
        #st.write(df["Ex-Showroom_Price"].unique()) # no missing values present but has obj that needs to be converted
        df["Ex-Showroom_Price"] = df["Ex-Showroom_Price"].str.replace("Rs.", "").astype(str)
        df["Ex-Showroom_Price"] = df["Ex-Showroom_Price"].str.replace(",", "").astype(int)
        st.write(df["Ex-Showroom_Price"].unique())
    #st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#C9DEF5;" /> """, unsafe_allow_html=True)
    



    with st.container():
        left_column, mid_column, right_column = st.columns(3) 
    with left_column:
        st.write("Fuel Type")    
        st.write(df["Fuel_Type"].unique()) # <NA> values and obj present
        df[~df["Fuel_Type"].isna()]
    with right_column:
        st.write("Fuel Tank Capacity")     
        df = df[~df["Fuel_Tank_Capacity"].isna()]
        df["Fuel_Tank_Capacity"] = df["Fuel_Tank_Capacity"].str.split(" ").str.get(0).str.replace(",","")
        df = df[df["Fuel_Tank_Capacity"].str.isnumeric()]
        df["Fuel_Tank_Capacity"]=df["Fuel_Tank_Capacity"].astype(int)
        st.write( df["Fuel_Tank_Capacity"].unique())
    with mid_column: 
        st.write("Body Type") 
        df = df[~df["Body_Type"].isna()]   
        st.write(df["Body_Type"].unique()) # <NA> values and obj present


    with st.container():
        left_column, mid_column, right_column = st.columns(3)

    with left_column: 
        st.write("Height")     
        df = df[~df["Height"].isna()]
        df["Height"] = df["Height"].str.split(" ").str.get(0).str.replace(",","")
        df = df[df["Height"].str.isnumeric()]
        df["Height"]=df["Height"].astype(int)
        st.write(df["Height"].unique()) # <NA> values and obj present
    

    with right_column:
        st.write("Length")  
        df = df[~df["Length"].isna()]
        df["Length"] = df["Length"].str.split(" ").str.get(0).str.replace(",","")
        df = df[df["Length"].str.isnumeric()]
        df["Length"]=df["Length"].astype(int)   
        st.write(df["Length"].unique()) # <NA> values and obj present

    with mid_column:
        st.write("Width")   
        df = df[~df["Width"].isna()]
        df["Width"] = df["Width"].str.split(" ").str.get(0).str.replace(",","")
        df = df[df["Width"].str.isnumeric()]
        df["Width"]=df["Width"].astype(int)  
        st.write(df["Width"].unique()) # <NA> values and obj present


    with st.container():
        left_column, mid_column, right_column = st.columns(3)

    with left_column: 
        st.write("City Mileage")     
     # <NA> values and obj present
        df = df[~df["City_Mileage"].isna()]
        df["City_Mileage"] = df["City_Mileage"].str.split(" ").str.get(0).str.replace(",","")
        #df["City_Mileage"] = df["City_Mileage"].astype(int)
        st.write(df["City_Mileage"].unique())
    
    with right_column:
        st.write("Highway Mileage")     
     # <NA> values and obj present
        df = df[~df["Highway_Mileage"].isna()]
        df["Highway_Mileage"] = df["Highway_Mileage"].str.split(" ").str.get(0).str.replace(",","")
        #df["City_Mileage"] = df["City_Mileage"].astype(int)
        st.write(df["Highway_Mileage"].unique())
    with mid_column: 
        st.write("Type")    
        df = df[~df["Type"].isna()]
        st.write(df["Type"].unique()) # <NA> value present

    # Cleaning of data

    backup = df.copy()
    df.to_csv("Cleaned_data.csv")

    
