import streamlit as st
from utils import db_functions

def physician_dashboard():
    st.title("Physician Dashboard")

    st.subheader("Patient Summary")

    # Fetch and display processed data from the database (e.g., wearables)
    patient_data = db_functions.fetch_patient_metrics(user_id=1)  # Replace with actual user ID logic

    st.write("Sleep Metrics:")
    st.write(f"Average hours of sleep this week: {patient_data['avg_sleep']} hours")
    st.write(f"Sleep quality: {patient_data['sleep_quality']}")

    st.write("Exercise Metrics:")
    st.write(f"Steps this week: {patient_data['steps']}")

    # Charts comparing current and historical data
    st.line_chart(patient_data['sleep_over_time'])
    st.line_chart(patient_data['steps_over_time'])
