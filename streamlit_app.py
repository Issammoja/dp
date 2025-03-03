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
 
# Initialize session state to store input features
if 'input_features' not in st.session_state:
    st.session_state.input_features = pd.DataFrame(columns=[
        'Month', 'Rainfall (MM)', 'Season', 'Total_Rainfall', 
        'Avg_Rainfall', 'Max_Rainfall', 'Min_Rainfall', 'Rainfall_Lag1'
    ])

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

    # Button to add the current input to the DataFrame
    if st.button('Add to DataFrame'):
        # Create a new row with the input features
        new_row = {
            'Month': month,
            'Rainfall (MM)': rainfall_mm,
            'Season': season,
            'Total_Rainfall': total_rainfall,
            'Avg_Rainfall': avg_rainfall,
            'Max_Rainfall': max_rainfall,
            'Min_Rainfall': min_rainfall,
            'Rainfall_Lag1': rainfall_lag1
        }

        # Append the new row to the session state DataFrame
        st.session_state.input_features = st.session_state.input_features.append(new_row, ignore_index=True)

# Display the DataFrame
st.header('Input Features DataFrame')
st.dataframe(st.session_state.input_features)

# Option to clear the DataFrame
if st.button('Clear DataFrame'):
    st.session_state.input_features = pd.DataFrame(columns=[
        'Month', 'Rainfall (MM)', 'Season', 'Total_Rainfall', 
        'Avg_Rainfall', 'Max_Rainfall', 'Min_Rainfall', 'Rainfall_Lag1'
    ])
  
  
