# Text-to-Speech
Sure! Let's break down the libraries used in your Text-to-Speech (TTS) project and explain how they work step by step:

### 1. **`tkinter`**
   - **Purpose**: `tkinter` is the standard Python library for creating graphical user interfaces (GUIs). It allows you to build windows, buttons, labels, text boxes, and more.
   - **How it works**:
     - You import `tkinter` (or `tk` for short) to create GUI components like buttons, labels, text boxes, and windows.
     - `ttk` is a submodule of `tkinter` that provides modern-looking widgets, such as `Combobox`, `Treeview`, etc.
     - You use `root = tk.Tk()` to create a root window that holds all the widgets.
     - Widgets are added to the window using methods like `.pack()`, `.grid()`, or `.place()`.
     - Finally, `root.mainloop()` keeps the window open and listens for user interaction (button clicks, text input, etc.).

   - **In your code**: 
     - `tk.Label`, `tk.Text`, `ttk.Combobox`, and `tk.Button` are used to create the GUI components.
     - The `status_label` and `text_input` widgets are used to display messages and capture user input.

### 2. **`gTTS` (Google Text-to-Speech)**
   - **Purpose**: `gTTS` is a library that interfaces with Google’s Text-to-Speech API. It converts text into spoken audio.
   - **How it works**:
     - `gTTS` takes a string of text and a language code (like `en` for English, `es` for Spanish, etc.).
     - It sends the text to Google's API, which returns an audio file (in `.mp3` format) containing the spoken text.
     - You can specify the language for speech output using the `lang` parameter.
     - The resulting audio file is saved locally as a `.mp3` file.

   - **In your code**:
     - The function `gTTS(text, lang=language)` is used to create the audio from the input text.
     - The `tts.save("output.mp3")` line saves the audio as an `output.mp3` file.
     - After saving, the file is played back using `pygame` and removed once it's finished.

### 3. **`pygame`**
   - **Purpose**: `pygame` is a library used to handle multimedia tasks, such as playing sound, music, and graphics.
   - **How it works**:
     - The `pygame.mixer` module is used for playing audio in various formats (like `.mp3`, `.wav`).
     - The `pygame.mixer.init()` initializes the audio mixer so that you can use it to play sounds.
     - `pygame.mixer.music.load("output.mp3")` loads the audio file.
     - `pygame.mixer.music.play()` starts playing the audio.
     - The `while pygame.mixer.music.get_busy()` loop ensures that the program waits until the audio finishes before proceeding to delete the file.

   - **In your code**:
     - After generating the `.mp3` file, the code uses `pygame.mixer` to play it.
     - The `while pygame.mixer.music.get_busy()` ensures the program waits for the audio to finish before removing the file.

### 4. **`os`**
   - **Purpose**: The `os` library provides functions for interacting with the operating system, such as handling files and directories.
   - **How it works**:
     - `os.remove("output.mp3")` deletes the file after it has been played to free up space and avoid leaving unused files.

   - **In your code**:
     - After the audio finishes playing, the `os.remove()` function is called to delete the temporary `output.mp3` file that was created by `gTTS`.

### Step-by-Step Flow of How the Code Works:
1. **GUI Creation**: 
   - When the program starts, a window (`root`) is created using `tkinter`. The window contains a label, a text input box, a language dropdown (for selecting the language), a button to trigger the text-to-speech function, and a status label.
   
2. **User Interaction**:
   - The user enters text into the text input box and selects a language from the dropdown (like English `en`, Spanish `es`, French `fr`).
   - The user clicks the "Text-to-Speech" button.

3. **Text-to-Speech Process**:
   - The `text_to_speech()` function is triggered when the button is clicked.
   - The text entered by the user is retrieved using `text_input.get("1.0", tk.END)`.
   - The `gTTS` library is used to convert the text to an audio file (`output.mp3`), using the selected language.
   - The audio file is saved locally on the system.

4. **Play Audio**:
   - The `pygame.mixer` module is used to load and play the audio file (`output.mp3`).
   - The program waits for the audio to finish playing (using `pygame.mixer.music.get_busy()`), ensuring that the audio is fully played before proceeding.

5. **File Cleanup**:
   - After the audio has finished, the temporary `output.mp3` file is deleted using `os.remove("output.mp3")` to avoid leaving unused files on the system.

6. **Status Update**:
   - After the TTS process is completed, the status label updates to show the message "TTS Completed!" in green. If there was no input text, it will show "Please enter text!" in red.

### Summary of Libraries Used:
- **`tkinter`**: For building the GUI interface.
- **`gTTS`**: For converting the text entered by the user to speech (audio).
- **`pygame`**: For playing the generated speech audio.
- **`os`**: For deleting the generated audio file after playback.

This is how the code works to provide a Text-to-Speech tool with a simple GUI interface!
