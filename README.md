#  Copilot Wakeup call process

This project enables voice-based interaction with **Windows Copilot** (or any app that supports text input) using **speech recognition**, **keyboard automation**, and **UI Automation** in Python.

---

## ✨ Features

- ✅ **Wake Word Activation** – Starts the assistant when you say **"hello"**.
- ✅ **Voice Input to Copilot** – Converts speech to text and sends it to the Copilot input box.
- ✅ **Audible Feedback** – Plays sounds on wake and response.
- ✅ **Exit Command** – Say **"exit"** to close the Copilot window or **"stop"** to terminate the program.
- ✅ **Error Handling** – Gracefully handles unrecognized speech and connection errors.

---

## 🛠 Tech Stack

- **Python** 3.x
- **Libraries Used**:
  - `speech_recognition` – For speech-to-text
  - `keyboard` – To simulate keyboard shortcuts
  - `uiautomation` – For Windows UI control
  - `winsound` – For sound notifications
  - `threading` *(optional if expanded)*

---

## 📂 Project Structure

voice-controlled-copilot/
│
├── main.py          # The main script
├── ding1.wav        # Sound for wake confirmation
├── ding2.wav        # Sound for recognized input
└── README.md        # Documentation


---

## ⚙️ Setup & Installation

### 1. **Clone the Repository**
```bash
git clone https://github.com/your-username/voice-controlled-copilot.git
cd voice-controlled-copilot

### 2. **Install Dependencies**

```bash
pip install speechrecognition keyboard uiautomation
```

> **Note**: On Windows, you may need:

```bash
pip install pyaudio
```

If `pyaudio` fails to install:

```bash
pip install pipwin
pipwin install pyaudio
```

### 3. **Add Sound Files**

Ensure `ding1.wav` and `ding2.wav` exist in the project root.

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

* Say **"hello"** to wake the assistant and open Copilot.
* Speak your query – it will be typed into Copilot and submitted.
* Say **"exit"** to close Copilot, or **"stop"** to terminate the program.

---

## 🔑 Key Functions

| Function              | Purpose                                  |
| --------------------- | ---------------------------------------- |
| `inputwait()`         | Listens for voice input and returns text |
| `callcopilot()`       | Opens Copilot using `Alt + Space`        |
| `asktocopilot()`      | Sends recognized text to Copilot         |
| `waitforwakeupcall()` | Listens for the wake word `"hello"`      |

---

## ✅ To-Do / Future Improvements

* 🔍 Add **hotword detection** without blocking the main thread.
* 🌐 Support **multiple languages** for voice recognition.
* 💡 Integrate with **other AI assistants** beyond Copilot.
* 🎛 GUI for configuration (sounds, keywords, etc.).

---

## ⚠️ Notes

* Requires **Windows** (due to `uiautomation` and `winsound`).
* Microphone access is necessary.
* Works best in a quiet environment.

---

## 📜 License

This project is licensed under the **MIT License**.

