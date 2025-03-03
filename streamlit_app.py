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


# Sidebar for input features
with st.sidebar:
    st.header('Input features')

    # Month selection
    month = st.selectbox('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

    # Rainfall slider
    rainfall_mm = st.slider('Rainfall (mm)', 0.0, 250.0, 50.0)  # Min: 0, Max: 250, Default: 50

    # Seasonal selection
    season = st.selectbox('Season', ('Dry', 'Wet'))

    # Yearly statistics sliders
    total_rainfall = st.slider('Total Annual Rainfall (mm)', 0.0, 2000.0, 1000.0)  # Min: 0, Max: 2000, Default: 1000
    avg_rainfall = st.slider('Average Monthly Rainfall (mm)', 0.0, 200.0, 50.0)  # Min: 0, Max: 200, Default: 50
    max_rainfall = st.slider('Maximum Monthly Rainfall (mm)', 0.0, 250.0, 100.0)  # Min: 0, Max: 250, Default: 100
    min_rainfall = st.slider('Minimum Monthly Rainfall (mm)', 0.0, 100.0, 10.0)  # Min: 0, Max: 100, Default: 10

    # Lag feature (rainfall from the previous month)
    rainfall_lag1 = st.slider('Rainfall (Previous Month) (mm)', 0.0, 250.0, 40.0)  # Min: 0, Max: 250, Default: 40
  
  
