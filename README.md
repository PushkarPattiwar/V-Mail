# V-Mail: Empowering Visually Impaired Communication  

V-Mail is an advanced voice-controlled email system designed to enhance accessibility for visually impaired users. It leverages cutting-edge technologies such as Speech-to-Text (STT), Text-to-Speech (TTS), and facial recognition to ensure seamless, hands-free email communication.  

## Table of Contents  

1. [Features](#features)  
2. [System Modules](#system-modules)  
3. [Technologies Used](#technologies-used)  
4. [Getting Started](#getting-started)  

---

## Features  

- **Voice-Driven Commands**: Compose, send, read, and manage emails through voice.  
- **Facial Recognition**: Secure and efficient user authentication.  
- **Email Management**: Read emails aloud, attach files, and organize inbox using voice commands.  
- **Error Handling**: Handles noisy environments, unclear commands, and incorrect inputs gracefully.  
- **User-Centric Design**: Built with accessibility standards to prioritize visually impaired users.  

---

## System Modules  

### 1. Voice Recognition Module  
- **Purpose**: Recognizes and processes user voice commands.  
- **Technologies**: Google Speech API, Python's `speech_recognition`.  

### 2. Face Recognition Module  
- **Purpose**: Authenticates users securely using facial recognition.  
- **Technologies**: Face Recognition API, `cv2`.  

### 3. Email Composition Module  
- **Purpose**: Enables users to compose and send emails using voice commands.  
- **Technologies**: SMTP for email delivery, TTS for confirmation.  

### 4. Email Reading Module  
- **Purpose**: Reads emails aloud using TTS technology.  
- **Technologies**: IMAPClient for fetching emails, `pyttsx3` for TTS.  

### 5. Attachment Module  
- **Purpose**: Facilitates voice-controlled file attachments.  

### 6. User Session Management  
- **Purpose**: Manages login, authentication, and session states.  

### 7. Graphical User Interface (GUI)  
- **Purpose**: Provides an interactive interface designed for voice-driven navigation.  
- **Technologies**: Tkinter for GUI.  

---

## Technologies Used  

- **Frontend**: Tkinter  
- **Backend**: Python with modules like `speech_recognition`, `pyttsx3`, and `cv2`.  
- **APIs**: Google Speech API, Face Recognition API.  
- **Email Handling**: SMTP for sending, IMAP for fetching emails.  

---

## Getting Started  

### Prerequisites  

- Python 3.x installed on your system.  
- Required libraries: `speech_recognition`, `pyttsx3`, `cv2`, `imapclient`, `smtplib`, `tkinter`.  

### Installation  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/yourusername/v-mail.git  
   cd v-mail

2. Install Dependencies  
   Use the following command to install all the necessary dependencies for the project:  
   ```bash
   pip install -r requirements.txt

3. Run the Application  
   After successfully installing the dependencies, start the application with the following command:  
   ```bash
   python main.py


