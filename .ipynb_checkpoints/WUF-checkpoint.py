import threading
import speech_recognition as sr
import keyboard
import uiautomation as auto
import winsound

# Create a recognizer instance for speech recognition
r = sr.Recognizer()

# Function to capture voice input and return recognized text
def inputwait(tout=None, ptlim=None):
    while True:
        with sr.Microphone() as source:
            # Listen for audio input with optional timeout and phrase limit
            audio_input = r.listen(source, timeout=tout, phrase_time_limit=ptlim)
            try:
                # Use Google Speech Recognition to convert audio to text
                text = r.recognize_google(audio_input)
                return text
            except sr.WaitTimeoutError:
                # If timeout occurs, ignore and continue
                None
            except sr.UnknownValueError:
                # If speech is unintelligible, ignore and continue
                None
            except sr.RequestError as e:
                # If there's an API error or connection issue, ignore
                None

# Function to open Copilot using Alt + Space
def callcopilot():
    keyboard.press('alt')
    keyboard.press_and_release('space')
    keyboard.release('alt')

# Function to interact with Copilot after opening it
def asktocopilot():
    # Find the Copilot window
    copilot_window = auto.WindowControl(Name='Copilot')
    if not copilot_window.Exists(3, 1):
        return

    # Access the input text box inside Copilot
    input_box = copilot_window.EditControl(AutomationId="InputTextBox")

    # Get the value pattern for text input
    value_pattern = input_box.GetValuePattern()

    while True:
        # Wait for voice input
        text = inputwait()
        # Play notification sound when input is captured
        winsound.PlaySound("ding2.wav", winsound.SND_FILENAME)

        # If user says "exit", close Copilot and break the loop
        if text.lower() == "exit":
            if copilot_window.Exists(3):
                close_button = copilot_window.ButtonControl(AutomationId="Close")
                if close_button.Exists(3):
                    close_button.GetInvokePattern().Invoke()
                break
            else:
                break

        # Set the recognized text into Copilot input box
        value_pattern.SetValue(text)
        # Press Enter to submit the input
        auto.SendKeys("{Enter}")

# Main function to listen for wake-up call
def waitforwakeupcall():
    while True:
        # Wait for a trigger word
        call = inputwait()
        # If user says "hello", open Copilot and start interaction
        if call.lower() == "hello":
            winsound.PlaySound("ding1.wav", winsound.SND_FILENAME)
            callcopilot()
            asktocopilot()
        # If user says "stop", exit the loop
        if "stop" in call.lower():
            break

# Entry point of the script
if __name__ == "__main__":
    waitforwakeupcall()
