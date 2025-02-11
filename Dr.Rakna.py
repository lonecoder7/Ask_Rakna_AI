"""
  title: Ask Dr.Rakna
  author :Rakna
  Date: 5-01-2025
"""

import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os
from response_logic import get_healthcare_response  
 
st.title("ASK Dr.Rakna 🩺")
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
        text-align: left;  
        color: black;
        margin: 10px 0;
        padding: 10px;
        border-radius: 10px;
        background-color: #e1f5fe;  
        display: inline-block;
        max-width: 70%;
    }
    .bot-message {
        text-align: right;  
        color: black;
        margin: 10px 0;
        padding: 10px;
        border-radius: 10px;
        background-color: #c8e6c9;  
        display: inline-block;
        max-width: 70%;
        float: right;  
    }
    </style>
    """,
    unsafe_allow_html=True
)

recognizer = sr.Recognizer()

def speak_text(command):
    if command:  # Check if command is not empty
        tts = gTTS(text=command, lang='en')
        tts.save("temp.mp3")
        os.system("start temp.mp3")  # For Windows
    else:
        st.error("unable to process please try again!")

if 'conversation' not in st.session_state:
    st.session_state.conversation = []

for message in st.session_state.conversation:
    if "User   " in message:
        st.markdown(f"<div class='user-message'>{message}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-message'>{message}</div>", unsafe_allow_html=True)

user_input = st.text_input("How can I help you:")

if st.button("Send"):
    if user_input:
        st.session_state.conversation.append(f":User   {user_input}")
        response = get_healthcare_response(user_input.lower())
        st.session_state.conversation.append(f"Dr.Rakna: {response}")
        speak_text(response)  # Call speak_text for each response

if st.button("Speak to Assistant"):
    with st.spinner("Listening..."):
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.2)
                audio = recognizer.listen(source)
                recognized_text = recognizer.recognize_google(audio)
                recognized_text = recognized_text.lower()
                st.session_state.conversation.append(f":User   {recognized_text}")
              
                response = get_healthcare_response(recognized_text)
                st.session_state.conversation.append(f"Dr.Rakna: {response}")

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
