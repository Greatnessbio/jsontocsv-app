import streamlit as st
import json
import pandas as pd
import io

def json_to_dataframe(json_data):
    # Extract organic_results from the JSON data
    organic_results = json_data.get('organic_results', [])
    
    # Convert to DataFrame
    df = pd.json_normalize(organic_results)
    
    return df

st.title('JSON to CSV Converter')

uploaded_file = st.file_uploader("Choose a JSON file", type="json")

if uploaded_file is not None:
    # Read the file
    json_data = json.load(uploaded_file)
    
    # Convert JSON to DataFrame
    df = json_to_dataframe(json_data)
    
    # Display the data
    st.write("### Data Preview")
    st.dataframe(df)
    
    # Provide download link for CSV
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name="converted_data.csv",
        mime="text/csv",
    )
