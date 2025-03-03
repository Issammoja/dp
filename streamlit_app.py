import streamlit as st
import pandas as pd
import altair as alt



st.title('Early Drought Warning System')

st.info('This app builds a predictive model using regression model')
with st.expander('Data'):
  st.write('**Raw data**')
  df= pd.read_csv('https://raw.githubusercontent.com/Issammoja/dp/refs/heads/master/kenya-climate-data-1991-2016-rainfallmm.csv')
  df
  
  st.write('**X**')
  X_raw = df.drop('Year', axis = 1)
  X_raw

  st.write('**y**')
  y_raw = df.Year
  y_raw

with st.expander('Data visualization'):

  st.bar_chart(data=df, x='Year', y='Rainfall - (MM)')

# Data Preparation
with st.sidebar:
  st.header('Input Feautures')
 
# Select Month
month_options = df["Month_Average"].unique().tolist()
selected_month = st.sidebar.selectbox("Select Month", month_options)



  
  
