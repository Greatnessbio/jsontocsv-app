import streamlit as st
import json
from streamlit_javascript import st_javascript

# Load the JSON data
with open('elisa_kits_data.json', 'r') as file:
    data = json.load(file)

# Extract organic results
organic_results = data['organic_results']

# Create Streamlit app
st.set_page_config(page_title="ELISA Kits Search Results", layout="wide")

# Use the custom React component
st_javascript("""
import React from 'react';
import ReactDOM from 'react-dom';
import ElisaKitsTable from './elisa-kits-table';

ReactDOM.render(
  <ElisaKitsTable data={organic_results} />,
  document.getElementById('react-table')
)
""")

# Create a placeholder for the React component
st.components.v1.html('<div id="react-table"></div>', height=600)
