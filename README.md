# Ask_Dr_Rakna

Ask_Dr_Rakna is an AI-powered healthcare chatbot with speech-to-text and text-to-speech capabilities. Built with **Streamlit**, this application enables users to interact with an AI assistant via both text and voice, providing quick and reliable health-related responses.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction
Ask_Dr_Rakna is a chatbot designed to assist users with healthcare-related inquiries. It integrates **speech recognition** for voice input and **text-to-speech** for responses, offering an intuitive and accessible communication experience. The chatbot follows predefined response logic but can be extended for more dynamic AI-powered interactions.

---

## Features
- **Text-based Chat**: Users can type their queries to receive responses.
- **Voice Interaction**: Allows users to speak to the assistant, which processes and responds accordingly.
- **Healthcare-focused Responses**: Provides relevant health-related information.
- **Text-to-Speech (TTS)**: Reads out chatbot responses for enhanced accessibility.
- **User Feedback**: Collects ratings and feedback for continuous improvement.

---

## Installation

### Prerequisites:
- Python 3.7+
- Install required dependencies using:

```sh
pip install streamlit speechrecognition gtts
```

---

## Usage

1. **Clone the repository**:

   ```sh
   git clone https://github.com/your-username/ask-dr-rakna.git
   ```

2. **Navigate to the project directory**:

   ```sh
   cd ask-dr-rakna
   ```

3. **Run the Streamlit app**:

   ```sh
   streamlit run app.py
   ```

4. The application will open in your browser, where you can start interacting with the chatbot via text or voice input.

---

## Customization
Modify `response_logic.py` to add predefined answers or integrate an AI model for dynamic responses.

---

## Future Enhancements
- Improve response accuracy using advanced NLP models.
- Implement analytics for tracking user interactions.
- Add multilingual support.

---

## Contributing
Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push your branch to your forked repository.
5. Submit a Pull Request to the main repository.

---

## License
This project is licensed under the MIT License.

