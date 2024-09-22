import streamlit as st
from utils import db_functions

def home_page():
    st.title("Postpartum Care Monitoring")
    st.write("Log your mood, energy, and other factors:")

    # Mood tracker
    mood = st.slider("Mood (1: low, 10: high)", 1, 10, 5)

    # Energy and sleep
    energy = st.slider("Energy levels", 1, 10, 5)
    sleep_quality = st.slider("Sleep quality", 1, 10, 5)
    
    # Submit data
    if st.button("Submit"):
        db_functions.log_data_to_db(mood, energy, sleep_quality)
        st.success("Your data has been logged successfully!")
