import requests
import streamlit as st
import plotly.express as px
from PIL import Image
import pandas as pd
from streamlit_lottie import st_lottie
import matplotlib.pyplot as plt
import seaborn as sn
import sqlite3
conn = sqlite3.connect("data.db", check_same_thread=False)
cur = conn.cursor()

def app():
    def form():
        st.write("Enquiry Form")
        with st.form(key="Information Form"):
            name = st.text_input("Enter Your Name:")
            email = st.text_input("Enter your email:")
            issue = st.text_input("Enter Query:")
            modeln = st.text_input("Enter Model Name")
            submission = st.form_submit_button(label="Submit")
            if submission == True:
                addData(name,email,issue,modeln)
    def addData(a,b,c,d):
        cur.execute("""CREATE TABLE IF NOT EXISTS form1(NAME TEXT(50), EMAIL TEXT(50), ISSUE TEXT(50), MODELN TEXT(50));""")
        cur.execute("INSERT INTO form1 VALUES(?,?,?,?)",(a,b,c,d))
        conn.commit()
        conn.close()
        st.success("Successfully submitted")

    form()
