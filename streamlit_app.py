import streamlit as st
import pandas as pd



st.title('Early Drought Warning System')

st.info('This app builds a predictive model using regression model')
with st.expander('Data'):
  st.write('**Raw data**')
  df= pd.read_csv('https://raw.githubusercontent.com/Issammoja/dp/refs/heads/master/kenya-climate-data-1991-2016-rainfallmm.csv')
  df
  st.write('**x**')
  x = df.drop('year', axis=1)
  x
  st.write('**y**')
  y = df.drop('rainfall')
