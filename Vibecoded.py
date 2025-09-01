import subprocess
import time
import speech_recognition as sr
import pyttsx3
import uiautomation as auto
import win32gui
import win32con
import tkinter as tk
import threading

# ------------------------------
# Text-to-Speech (Optional)
# ------------------------------
engine = pyttsx3.init()
engine.setProperty('rate', 175)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ------------------------------
# Custom Floating UI
# ------------------------------
def show_ui(status_text="Listening..."):
    def run_ui():
        root = tk.Tk()
        root.title("Copilot Assistant")
        root.geometry("320x120+100+100")
        root.configure(bg="#1e1e1e")
        root.overrideredirect(True)  # No title bar
        root.attributes("-topmost", True)

        label = tk.Label(root, text=status_text, fg="white", bg="#1e1e1e", font=("Segoe UI", 16))
        label.pack(expand=True)

        # Auto-close after 6 seconds
        root.after(6000, root.destroy)
        root.mainloop()

    threading.Thread(target=run_ui).start()

# ------------------------------
# Hide Edge (Copilot) Window
# ------------------------------
def hide_edge_window():
    time.sleep(5)  # Wait for Copilot to load
    hwnd = win32gui.FindWindow(None, "Microsoft Edge")
    if hwnd:
        win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
        print("[+] Edge window hidden")
    else:
        print("[!] Edge window not found")

# ------------------------------
# Activate Copilot Mic
# ------------------------------
def activate_copilot_mic():
    print("[*] Activating Copilot voice input...")
    edge_window = auto.WindowControl(searchDepth=1, ClassName='Chrome_WidgetWin_1')
    mic_button = edge_window.ButtonControl(Name="Start voice input")
    if mic_button.Exists(5):
        mic_button.Click()
        print("[+] Mic activated!")
    else:
        print("[!] Mic button not found")

# ------------------------------
# Launch Copilot
# ------------------------------
def launch_copilot():
    print("[*] Launching Copilot...")
    subprocess.Popen(['explorer', 'microsoft-edge://?ux=copilot&source=taskbar'])
    time.sleep(5)

# ------------------------------
# Voice Wake Word Detection
# ------------------------------
def listen_for_wake_word():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("[*] Listening for wake word: 'Hey Copilot'...")
        while True:
            try:
                audio = r.listen(source)
                text = r.recognize_google(audio).lower()
                print(f"[DEBUG] Heard: {text}")
                if "hey copilot" in text:
                    print("[+] Wake word detected!")
                    speak("Yes, how can I help?")
                    show_ui("Activating Copilot...")
                    start_copilot_process()
            except sr.UnknownValueError:
                continue
            except sr.RequestError:
                print("[!] Speech Recognition API error")
                continue

# ------------------------------
# Main Copilot Activation Flow
# ------------------------------
def start_copilot_process():
    launch_copilot()
    activate_copilot_mic()
    hide_edge_window()
    show_ui("Copilot Voice Ready!")

# ------------------------------
# Main Entry
# ------------------------------
if __name__ == "__main__":
    listen_for_wake_word()
