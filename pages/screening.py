import streamlit as st
from models import ppd_model

def screening_page():
    st.title("Postnatal Depression Screening")

    # Edinburgh Postnatal Depression Scale (EPDS)
    questions = [
        "I have been able to laugh and see the funny side of things",
        "I have looked forward with enjoyment to things",
        # Add other questions from the EPDS
    ]

    answers = []
    for question in questions:
        answer = st.radio(question, ['Yes', 'No'])
        answers.append(answer)

    if st.button("Analyze Results"):
        score = ppd_model.analyze_answers(answers)
        st.write(f"Your Postnatal Depression Score: {score}")
        if score >= 10:  # Example threshold for concern
            st.warning("You are at risk for postpartum depression. Please consult with a physician.")
