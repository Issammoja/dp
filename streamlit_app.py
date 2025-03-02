import streamlit as st
import pandas as pd

st.title('Early Drought Warning System')
st.info('This app builds a predictive model using a regression model')

with st.expander('Data'):
    st.write('**Raw data**')
    # Load the data
    df = pd.read_csv('https://raw.githubusercontent.com/Issammoja/dp/refs/heads/master/kenya-climate-data-1991-2016-rainfallmm.csv')
    
    # Display the raw data
    st.write(df)
    
    # Debug: Display column names
    st.write("Columns in the DataFrame:", df.columns.tolist())
    
    # Normalize column names (optional)
    df.columns = df.columns.str.strip().str.lower()
    
    # Drop the 'year' column
    st.write('**X**')
    X = df.drop('year', axis=1)  # Use the correct column name
    st.write(X)
  
