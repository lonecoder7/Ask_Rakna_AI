# Ask_Rakna_AI

Ask_Rakna_AI is an AI chatbot with speech-to-text and text-to-speech capabilities. Powered by **Llama 3.2** and integrated with **Streamlit**, this app lets users communicate with an AI via voice commands and responses. It combines the power of natural language understanding with the convenience of speech.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction
Ask_Rakna_AI is an interactive AI chatbot that allows users to engage with it through speech. It uses **Llama 3.2** as the core language model and integrates **speech-to-text** for input and **text-to-speech** for output. With a user-friendly **Streamlit** interface, users can seamlessly interact with the chatbot, making it a fun and efficient tool for various applications.

The app listens to your voice input, converts it to text, sends it to the chatbot, and then converts the chatbot's response back into speech.

---

## Features
- **Voice Interaction**: Speak to the chatbot and receive responses in audio form.
- **Text-to-Speech**: Converts the AI's text responses into speech using **pyttsx3**.
- **Speech-to-Text**: Transcribes your spoken input into text using **SpeechRecognition**.
- **Real-Time Feedback**: Get feedback using **streamlit_feedback** to rate your interactions.
- **Streamlit Interface**: A simple and interactive interface built with **Streamlit** for an engaging user experience.

---

## Installation

### Prerequisites:
- Python 3.x
- Ensure you have the required Python libraries installed. You can install them via `pip` by running the following command in your terminal:

```bash
pip install streamlit speechrecognition pyttsx3 nest_asyncio requests json time streamlit_feedback
```

---

## Usage

1. **Clone the repository**:

   ```bash
   git clone https://github.com/lonecoder7/Ask_Rakna_AI.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd Ask_Rakna_AI
   ```

3. **Run the Streamlit app**:

   ```bash
   streamlit run app.py
   ```

4. The app will open in your browser, and you can start interacting with the chatbot using voice commands.

---

## API Reference

### 1. **Speech-to-Text** (Using `speech_recognition`)

This function listens for speech and converts it to text.

```python
import speech_recognition as sr

recognizer = sr.Recognizer()

def listen_to_audio():
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
```

### 2. **Text-to-Speech** (Using `pyttsx3`)

This function converts text to speech for the chatbot's response.

```python
import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
```

### 3. **Chatbot Query (Using Llama 3.2)**

For chatbot interaction, you can integrate your API (Llama 3.2) for generating AI responses based on user input.

```python
import requests

def get_chatbot_response(query):
    url = "http://your-llama-api-endpoint"
    headers = {"Content-Type": "application/json"}
    payload = json.dumps({"text": query})
    response = requests.post(url, headers=headers, data=payload)
    return response.json().get('response', '')
```

### 4. **Real-Time Feedback** (Using `streamlit_feedback`)

Enable users to give feedback on their chatbot interaction experience.

```python
from streamlit_feedback import feedback

def get_feedback():
    user_feedback = feedback(label="How was your interaction?", options=["Excellent", "Good", "Average", "Poor"])
    return user_feedback
```

---

## Contributing

We welcome contributions! If you want to improve the project, follow these steps:
1. **Fork** the repository.
2. Create a **new branch** for your feature or bug fix.
3. **Commit** your changes.
4. **Push** your branch to your forked repository.
5. Submit a **Pull Request** to the main repository.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
