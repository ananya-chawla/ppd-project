import streamlit as st
from pages import home, screening, results, appointments, resources, physician, biomarkers

# Main navigation
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Screening", "Results", "Appointments", "Resources", "Physician Dashboard", "Biomarkers"])

    if page == "Home":
        home.home_page()
    elif page == "Screening":
        screening.screening_page()
    elif page == "Results":
        results.results_page()
    elif page == "Appointments":
        appointments.appointments_page()
    elif page == "Resources":
        resources.resources_page()
    elif page == "Physician Dashboard":
        physician.physician_dashboard()
    elif page == "Biomarkers":
        biomarkers.biomarkers_page()

if __name__ == "__main__":
    main()
