import streamlit as st
import pandas as pd



st.title('machine learning app')

st.info('This app builds a machine learning model')
df= pd.read_csv('https://raw.githubusercontent.com/Issammoja/dp/refs/heads/master/kenya-climate-data-1991-2016-rainfallmm.csv')
df
