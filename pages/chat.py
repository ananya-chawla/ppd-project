import streamlit as st
import os

# Function to load chat history from a file
def load_chat_history(chat_file):
    """Load the chat history from a text file."""
    if os.path.exists(chat_file):
        with open(chat_file, 'r') as f:
            return f.readlines()
    return []

# Function to save a new message to the chat history file
def save_message(chat_file, sender, message):
    """Save a new message to the chat history."""
    with open(chat_file, 'a') as f:
        f.write(f"{sender}: {message}\n")

# Main function to display the chat page
def chat_page():
    st.title("Patient-Physician Communication")

    # A text file to store the chat history (could be replaced by a database)
    chat_file = "chat_history.txt"

    # Display chat history
    st.subheader("Chat History")
    chat_history = load_chat_history(chat_file)
    
    if chat_history:
        for line in chat_history:
            st.write(line)
    else:
        st.write("No messages yet.")

    # Input section for sending messages
    st.subheader("Send a Message")
    sender = st.selectbox("Who are you?", ["Patient", "Physician"])
    message = st.text_area("Enter your message:")

    if st.button("Send"):
        if message.strip():  # Check if the message is not empty
            save_message(chat_file, sender, message)
            st.success("Message sent!")
        else:
            st.error("Please enter a valid message.")
        
        # Refresh the page to show the updated chat history
        st.experimental_rerun()

# Entry point to integrate with the main app
if __name__ == "__main__":
    chat_page()
