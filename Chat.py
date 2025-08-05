# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Imports
import os
import streamlit as st
import google.generativeai as genai

# Configure Gemini API key using environment variable
genai.configure(api_key=os.getenv("GOOGEL_API_KEY"))

# Initialize the Gemini model and create a chat session
model = genai.GenerativeModel(model_name="gemini-1.5-pro")
chat = model.start_chat(history=[])

# Function to get streamed response from Gemini
def get_gemini_response(user_input):
    response = chat.send_message(user_input, stream=True)
    return response

# Set up Streamlit page title and header
st.set_page_config(page_title="Gemini Chatbot Demo")
st.header("Gemini LLM Chat App with Chat History")

# Initialize session state to store the chat history across user inputs
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Input field for user to enter a message
user_input = st.text_input("Enter your message:", key="input")

# Button to start the chat and send message to Gemini
if st.button("Start the chat") and user_input:
    # Get streamed response from Gemini for the user input
    response_chunks = get_gemini_response(user_input)

    # Append the user's message to chat history in session state
    st.session_state["chat_history"].append(("You", user_input))

    # Display Gemini’s response chunk by chunk
    st.subheader("Gemini's Response:")
    full_response = ""
    for chunk in response_chunks:
        st.write(chunk.text)  # Display each response chunk
        full_response += chunk.text  # Concatenate for full message

    # Append the full Gemini response to chat history
    st.session_state["chat_history"].append(("Gemini", full_response))

# Display full chat history from session state
if st.session_state["chat_history"]:
    st.subheader("Chat History:")
    for speaker, message in st.session_state["chat_history"]:
        st.write(f"**{speaker}**: {message}")  # Show each message in history
