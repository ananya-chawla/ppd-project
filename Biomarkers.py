import streamlit as st
from utils import db_functions

def biomarkers_page():
    st.title("Biomarkers and Lab Results")
    
    st.subheader("Recent Lab Results")
    
    # Fetch lab results from database (mocked here)
    lab_results = db_functions.fetch_lab_results(user_id=1)  # Replace with actual user ID logic

    for result in lab_results:
        st.write(f"{result['biomarker']}: {result['value']} {result['unit']} (Normal Range: {result['normal_range']})")
