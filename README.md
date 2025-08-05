# LLM-Chat-Bot-with-history-using-Gemini-Pro
A simple Streamlit app that lets you chat with Google's Gemini 1.5 Pro using live response streaming and session-based chat history. Clean UI, fast setup, and easy integration with your Gemini API key.

# Gemini LLM Chatbot with Chat History

This is a simple Streamlit web app that integrates with Google's Gemini 1.5 Pro LLM to enable a chat experience with session-based history. The app allows users to send messages and view responses from Gemini, with all interactions stored and displayed for the duration of the session.

## Features

* ✅ Chat with Google's **Gemini 1.5 Pro** LLM  
* ✅ Live streaming of responses  
* ✅ Full chat history maintained using **Streamlit session state**  
* ✅ Simple and clean UI

## Setup Instructions

### **Clone the repository**

```cmd
git clone https://github.com/your-username/gemini-chatbot-app.git
cd gemini-chatbot-app
````

### **Create a virtual environment (optional but recommended)**

```cmd
conda create -p venv python==3.10 -y 
```

### **Install the required dependencies**

```cmd
pip install -r requirements.txt
```

### **Set up environment variables**

Create a `.env` file in the project directory and add your Gemini API key:

```
GOOGEL_API_KEY=your_gemini_api_key_here
```

### **Run the app**

```cmd
streamlit run app.py
```

## Example Usage

1. Enter your message in the text box.
2. Click on **"Start the chat"**.
3. The app streams Gemini’s response.
4. Scroll down to view the full chat history.

## Notes

* Make sure your Gemini API key has access to `gemini-1.5-pro`.
* This app only stores chat history in the current session. Once refreshed, the history is cleared.

---

**Developed by Arif**

