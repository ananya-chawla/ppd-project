import streamlit as st

def resources_page():
    st.title("Resources")
    st.write("Find specialists and therapists for postpartum care.")

    insurance = st.selectbox("Select your insurance", ["Aetna", "BlueCross", "Kaiser"])
    specialization = st.selectbox("Specialization", ["Postpartum Depression", "Anxiety", "Counseling"])

    st.write(f"Showing therapists near you who accept {insurance} and specialize in {specialization}:")

    # Example data
    st.write("Dr. Jane Doe - Specializes in Postpartum Depression - Accepts Aetna")
    st.write("Dr. John Smith - Specializes in Anxiety - Accepts Kaiser")
