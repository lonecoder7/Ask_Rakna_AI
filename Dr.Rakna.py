"""
  title: Ask Dr.Rakna
  author :Rakna
  Date: 5-01-2025
"""

import streamlit as st
import speech_recognition as sr
import pyttsx3
import nest_asyncio
import requests
import json
import time
from streamlit_feedback import streamlit_feedback

nest_asyncio.apply()
st.title("ASK Dr.RAKNA 🩺")
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://t3.ftcdn.net/jpg/04/32/00/16/360_F_432001656_j8BXReMAqYRiPHkZEstEMh6rcL1WgnQG.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    .user-message {
        text-align: left;  /* Align user messages to the left */
        color: black;
        margin: 10px 0;
        padding: 10px;
        border-radius: 10px;
        background-color: #e1f5fe;  /* Light blue for user messages */
        display: inline-block;
        max-width: 70%;
    }
    .bot-message {
        text-align: right;  /* Align bot messages to the right */
        color: black;
        margin: 10px 0;
        padding: 10px;
        border-radius: 10px;
        background-color: #c8e6c9;  /* Light green for bot messages */
        display: inline-block;
        max-width: 70%;
        float: right;  /* Aligns the message to the right */
    }
    </style>
    """,
    unsafe_allow_html=True
)

recognizer = sr.Recognizer()
engine = pyttsx3.init()
API_URL = "http://localhost:11434/api/generate"  


def speak_text(command):
    engine.say(command)
    engine.runAndWait()

@st.cache_data  
def get_model_response(prompt):
    attempts = 3  
    for attempt in range(attempts):
        try:
            response = requests.post(API_URL, json={"prompt": prompt, "model": "llama3.2"}, stream=True)
            if response.status_code ==200:
                full_response = ""
                for chunk in response.iter_lines():
                    if chunk:
                        chunk_data = chunk.decode("utf-8")
                        chunk_json = json.loads(chunk_data)
                        full_response += chunk_json.get("response", "")
                        if chunk_json.get("done", False):
                            break
                return full_response[:500] 
            else:
                return f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            if attempt < attempts - 1:
                time.sleep(2)  
            else:
                return f"Error: {str(e)}"

if 'conversation' not in st.session_state:
    st.session_state.conversation = []


for message in st.session_state.conversation:
    if "User   " in message:
        st.markdown(f"<div class='user-message'>{message}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-message'>{message}</div>", unsafe_allow_html=True)


user_input = st.text_input("Type your message here:")

if st.button("Send"):
    if user_input:
        st.session_state.conversation.append(f"::User          {user_input}")
        response = get_model_response(user_input.lower())
        st.session_state.conversation.append(f"Healthcare Assistant: {response}")
        speak_text(response)

if st.button("Speak to Assistant"):
    with st.spinner("Listening..."):
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.2)
                audio = recognizer.listen(source)
                recognized_text = recognizer.recognize_google(audio)
                recognized_text = recognized_text.lower()
                st.session_state.conversation.append(f"User:          {recognized_text}")
                response = get_model_response(recognized_text)
                st.session_state.conversation.append(f"Healthcare Assistant: {response}")
                speak_text(response)
        except sr.UnknownValueError:
            st.error("Sorry, I could not understand the audio.")
        except sr.RequestError:
            st.error("Could not request results from the speech recognition service.")


sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")

    additional_remarks = st.text_area("Please provide additional remarks:")

if st.button("Submit Feedback"):
    if additional_remarks:
        st.success("Thank you for your feedback!")