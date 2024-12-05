import tkinter as tk
from tkinter import ttk  # Import ttk
from gtts import gTTS
import pygame
import os

# Function: Convert Text to Speech
def text_to_speech():
    text = text_input.get("1.0", tk.END).strip()
    if text:
        language = lang_var.get()
        tts = gTTS(text, lang=language)
        tts.save("output.mp3")

        # Play audio using pygame
        pygame.mixer.init()
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # Wait until playback is finished
            continue
        os.remove("output.mp3")
        status_label.config(text="TTS Completed!", fg="green")
    else:
        status_label.config(text="Please enter text!", fg="red")

# Tkinter GUI Setup
root = tk.Tk()
root.title("Text-to-Speech Tool")
root.geometry("400x300")

# Title
tk.Label(root, text="Text-to-Speech", font=("Helvetica", 14)).pack(pady=10)

# Text Input Box
text_input = tk.Text(root, height=5, width=40)
text_input.pack(pady=10)

# Language Dropdown
lang_var = tk.StringVar(value="en")
lang_label = tk.Label(root, text="Select Language:")
lang_label.pack()
lang_dropdown = ttk.Combobox(root, textvariable=lang_var, values=["en", "es", "fr", "de", "hi"])
lang_dropdown.pack()

# Button
tts_button = tk.Button(root, text="Text-to-Speech", command=text_to_speech, bg="lightblue")
tts_button.pack(pady=5)

# Status Label
status_label = tk.Label(root, text="Ready", fg="green")
status_label.pack(pady=10)

# Run the App
root.mainloop()
