import streamlit as st
from utils import db_functions

def appointments_page():
    st.title("Appointments")
    
    st.subheader("Scheduled Appointments")
    appointments = db_functions.fetch_appointments(user_id=1)  # Replace with actual user ID logic

    for appointment in appointments:
        st.write(f"{appointment['date']} with {appointment['doctor']}")
    
    st.subheader("Schedule a New Appointment")
    appointment_date = st.date_input("Select a Date")
    if st.button("Schedule"):
        db_functions.schedule_appointment(user_id=1, date=appointment_date)
        st.success("Appointment scheduled successfully!")
