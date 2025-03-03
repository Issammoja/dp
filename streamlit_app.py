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


# Calculate dynamic values for sliders
rainfall_min = data['Rainfall - (MM)'].min()
rainfall_max = data['Rainfall - (MM)'].max()
rainfall_default = data['Rainfall - (MM)'].median()

total_rainfall_min = data.groupby('Year')['Rainfall - (MM)'].sum().min()
total_rainfall_max = data.groupby('Year')['Rainfall - (MM)'].sum().max()
total_rainfall_default = data.groupby('Year')['Rainfall - (MM)'].sum().median()

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

    # Rainfall slider (dynamic values from CSV)
    rainfall_mm = st.slider(
        'Rainfall (mm)', 
        float(rainfall_min), float(rainfall_max), float(rainfall_default)
    )

    # Seasonal selection
    season = st.selectbox('Season', ('Dry', 'Wet'))

    # Yearly statistics sliders (dynamic values from CSV)
    total_rainfall = st.slider(
        'Total Annual Rainfall (mm)', 
        float(total_rainfall_min), float(total_rainfall_max), float(total_rainfall_default)
    )

    # For other sliders, you can calculate similar dynamic values
    avg_rainfall = st.slider('Average Monthly Rainfall (mm)', 0.0, 200.0, 50.0)  # Example placeholder
    max_rainfall = st.slider('Maximum Monthly Rainfall (mm)', 0.0, 250.0, 100.0)  # Example placeholder
    min_rainfall = st.slider('Minimum Monthly Rainfall (mm)', 0.0, 100.0, 10.0)  # Example placeholder

    # Lag feature (rainfall from the previous month)
    rainfall_lag1 = st.slider('Rainfall (Previous Month) (mm)', 0.0, 250.0, 40.0)  # Example placeholder

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
        new_row_df = pd.DataFrame([new_row])  # Convert dictionary to DataFrame
        st.session_state.input_features = pd.concat([st.session_state.input_features, new_row_df], ignore_index=True)

# Display the DataFrame
st.header('Input Features DataFrame')
st.dataframe(st.session_state.input_features)

# Option to clear the DataFrame
if st.button('Clear DataFrame'):
    st.session_state.input_features = pd.DataFrame(columns=[
        'Month', 'Rainfall (MM)', 'Season', 'Total_Rainfall', 
        'Avg_Rainfall', 'Max_Rainfall', 'Min_Rainfall', 'Rainfall_Lag1'
    ])
  
  
