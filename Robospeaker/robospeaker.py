import pyttsx3
import tkinter as tk
from tkinter import messagebox

def speak_text():
    text = text_input.get()
    if not text.strip():
        messagebox.showwarning("Input Error", "Please enter some text to speak!")
        return
    engine.say(text)
    engine.runAndWait()

def quit_app():
    engine.say("Goodbye!")
    engine.runAndWait()
    root.destroy()

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

# Create the main GUI window
root = tk.Tk()
root.title("RoboSpeaker 1.1 by Omendra")
root.geometry("400x200")

# Add a label
label = tk.Label(root, text="Enter text to speak:", font=("Arial", 14))
label.pack(pady=10)

# Add an input field
text_input = tk.Entry(root, width=40, font=("Arial", 12))
text_input.pack(pady=10)

# Add Speak button
speak_button = tk.Button(root, text="Speak", command=speak_text, font=("Arial", 12), bg="green", fg="white")
speak_button.pack(pady=10)

# Add Quit button
quit_button = tk.Button(root, text="Quit", command=quit_app, font=("Arial", 12), bg="red", fg="white")
quit_button.pack(pady=5)

# Run the main loop
root.mainloop()

