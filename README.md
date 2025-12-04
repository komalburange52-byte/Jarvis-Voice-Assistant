# Jarvis-Voice-Assistant
A Python-based voice assistant (Jarvis) using SpeechRecognition, pyttsx3, Wikipedia API, web automation, music player, and email automation. This project can listen to your commands, speak responses, open websites, play music, tell time, and send emails.


Jarvis is a Python-based personal voice assistant capable of performing daily automation tasks such as opening websites, searching Wikipedia, playing music, telling time, and sending emails — all through voice commands.

This project is designed for beginners to understand how voice assistants work and how to integrate speech recognition, text-to-speech, automation, and email functionality in Python.


   ⭐ Features

- 🎤 *Voice Command Recognition*  
- 🔊 *Text-to-Speech Responses*  
- 🌐 *Open Websites (YouTube, Google, StackOverflow)*  
- 📚 *Wikipedia Search (Speaks 2-line Summary)*  
- 🎵 *Music Player (From Local Directory)*  
- ⏰ *Time Announcer*  
- 📧 *Email Sender using SMTP*  
- 💻 *Launch Apps (VS Code, etc.)*


    📂 Project Structure

Jarvis/ │ ├── jarvis.py        # Main Voice Assistant Program ├── README.md        # Documentation └── requirements.txt # Required Libraries

---

    🛠 Technologies Used

- Python 3.x  
- pyttsx3  
- SpeechRecognition  
- wikipedia  
- webbrowser  
- os  
- datetime  
- smtplib  

---

      📦 Installation

Install required dependencies:

bash
pip install pyttsx3 SpeechRecognition wikipedia

For microphone support:

pip install pyaudio

If PyAudio fails to install:

pip install pipwin
pipwin install pyaudio


---

🚀 How to Run

Clone the project:

git clone https://github.com/<your-username>/<your-repo>.git

Navigate to project folder:

cd Jarvis

Run:

python jarvis.py




⚠️ Gmail App-Password Required for Email

Google blocks access using normal passwords.
Follow these steps:

1. Turn ON 2-step verification


2. Go to App Passwords


3. Generate password for “Mail”


4. Use it inside sendEmail():



server.login('your-email@gmail.com', 'your-app-password')


---

🤖 Future Enhancements

Add wake word ("Hey Jarvis")

Add weather and news updates

Control system operations (shutdown, restart)

Add ChatGPT integration

Add GUI interface


---

📜 License

This project is licensed under the MIT License.
Feel free to modify and improve it!

---
   
   2. requirements.txt**  
Copy this into a file named **requirements.txt**:

txt
pyttsx3
SpeechRecognition
wikipedia
pyaudio

